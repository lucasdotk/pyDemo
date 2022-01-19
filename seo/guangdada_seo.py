import re
import json
import time
import datetime
import logging
import decimal
import concurrent
import traceback

from seo.category import CATEGORY
from seo.channel import CHANNEL
from seo.theme import THEME
from seo.es_util import get_es
from concurrent.futures._base import ALL_COMPLETED, as_completed

# 获取es实例
ES = get_es()
TIMEOUT = 120
ES_INDEX = 'sp_material_index'
# 循环获取时每次获取的数量
LOOP_SIZE = 100
# 文件保存位置
SAVE_DIRECTORY = "/home/work/data/seo_data/"
# 上线平台
OS_ANDROID = "安卓"
OS_APPLE = "IOS"
logger = logging.getLogger('guangdada_seo')


def multi_thread_calculate():
    """
    使用多线程生成SEO需要的json数据
    :return:
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        after = ""
        sort_number = 0
        logger.info("开始生成SEO需要的json数据...")
        while True:
            advertiser_list, after = get_all_advertiser(after)
            # 无法取到广告主后，结束程序
            if len(advertiser_list) == 0:
                logger.info(">>>>>>>>>>>共生成SEO数据{}条<<<<<<<<<<<".format(str(sort_number)))
                logger.info("所有广告主的SEO数据生成完毕！")
                break
            future_tasks = []
            for advertiser in advertiser_list:
                task = executor.submit(calculate_seo_data, advertiser, sort_number)
                future_tasks.append(task)
                sort_number += 1
            for future in as_completed(future_tasks):  # 迭代生成器
                try:
                    future.result()
                except Exception as e:
                    logger.error(e)
                    traceback.print_exc()


def get_all_advertiser(after):
    """
    获取所有分类为游戏的广告主
    @param after:
    @return:
    """
    body = {
        "size": 0,
        "track_total_hits": True,
        "query": {
            "bool": {
                "must": [
                    {
                        "term": {
                            "is_deleted": 0
                        }
                    },
                    {
                        "nested": {
                            "path": "advertisers",
                            "query": {
                                "bool": {
                                    "must": [
                                        {
                                            "term": {
                                                "advertisers.app_type": 1
                                            }
                                        }
                                    ]
                                }
                            }
                        }
                    }
                ]
            }
        },
        "aggs": {
            "aggs_nested": {
                "nested": {
                    "path": "advertisers"
                },
                "aggs": {
                    "domain_aggs": {
                        "composite": {
                            "size": LOOP_SIZE,
                            "sources": [
                                {
                                    "domain_deep": {
                                        "terms": {
                                            "field": "advertisers.domain.keyword"
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        }
    }
    if after:
        body['aggs']['aggs_nested']['aggs']['domain_aggs']['composite']['after'] = {"domain_deep": after}
    response = ES.search(index=ES_INDEX, body=body, request_timeout=TIMEOUT)
    if len(response['aggregations']['aggs_nested']['domain_aggs']['buckets']) == 0:
        logger.info("所有广告主都已经生成seo数据，任务结束！")
        return [], None
    after = response['aggregations']['aggs_nested']['domain_aggs']['after_key']['domain_deep']
    buckets = response['aggregations']['aggs_nested']['domain_aggs']['buckets']
    advertiser_list = []
    for bucket in buckets:
        advertiser_list.append(bucket["key"]["domain_deep"])
    return advertiser_list, after


def calculate_seo_data(advertiser_list, sort_number):
    """
    计算seo需要的数据主方法
    @param advertiser_list:
    @param sort_number:
    @return:
    """
    for advertiser_domain in advertiser_list:
        seo_data = {}
        logger.info("处理每个广告主的数据，当前广告主的domain是{}".format(advertiser_domain))
        body = {
            "size": 3,
            "track_total_hits": True,
            "query": get_common_query(advertiser_domain),
            "aggs": {
                "sum_groups": {
                    "sum": {
                        "field": "creative_group_count"
                    }
                },
                "max_time": {
                    "max": {
                        "field": "updated_at"
                    }
                },
                "min_time": {
                    "min": {
                        "field": "created_at"
                    }
                },
                "sum_days": {
                    "sum": {
                        "field": "days"
                    }
                },
                "platform_terms": {
                    "terms": {
                        "field": "platforms",
                        "size": 10
                    }
                },
                "ad_nested": {
                    "nested": {
                        "path": "advertisers"
                    },
                    "aggs": {
                        "theme_terms": {
                            "terms": {
                                "field": "advertisers.theme",
                                "size": 10
                            }
                        },
                        "category_terms": {
                            "terms": {
                                "field": "advertisers.category",
                                "size": 10
                            }
                        }
                    }
                }
            },
            "sort": [
                {
                    "heat": {
                        "order": "desc"
                    }
                }
            ]
        }
        response = ES.search(index=ES_INDEX, body=body, request_timeout=TIMEOUT)
        hit_data = response['hits']['hits'][0]['_source']
        current_advertiser = hit_data['advertisers'][0]
        # 获取广告主应用名称
        seo_data["%advertiser%"] = to_better(current_advertiser['advertiser_name'])
        # 获取图标
        seo_data["%logo%"] = current_advertiser['logo_url']
        # 获取上线平台
        seo_data["%ai%"] = OS_ANDROID if current_advertiser['os'] == 1 else OS_ANDROID
        # 获取创意组数
        seo_data["%creative_groups%"] = response['aggregations']['sum_groups']['value']
        # 获取总投放天数
        seo_data["%days%"] = response['aggregations']['sum_days']['value']
        # 获取总投放时间
        start_timestamp = response['aggregations']['min_time']['value']
        end_timestamp = response['aggregations']['max_time']['value']
        seo_data["%period%"] = "{}~{}".format(datetime.datetime.fromtimestamp(start_timestamp),
                                              datetime.datetime.fromtimestamp(end_timestamp))

        # 获取广告主投放的所有平台
        seo_data['%network%'] = get_array_form_buckets(response['aggregations']['platform_terms']['buckets'],
                                                       'platform')
        # 获取广告主投放的所有类别
        seo_data['%categories%'] = get_array_form_buckets(
            response['aggregations']['ad_nested']['category_terms']['buckets'], 'category')
        # 获取广告主投放的所有主题
        seo_data['%theme%'] = get_array_form_buckets(response['aggregations']['ad_nested']['theme_terms']['buckets'],
                                                     'theme')

        # 计算广告主投放图片和视频的比例
        seo_data['%date%'] = time.strftime("%Y-%m-%d", time.localtime())
        type_buckets = response['aggregations']['type_terms']['buckets']
        type_dic = {
            "photo": 0,
            "video": 0
        }
        sum_type = 0
        for bucket in type_buckets:
            sum_type += bucket['doc_count']
            if bucket['key'] == 2:
                type_dic['video'] += bucket['doc_count']
                continue
            type_dic['photo'] += bucket['doc_count']
        seo_data['%photo%'] = "{}%".format(str(round(type_dic['photo'] / sum_type, 2)))
        seo_data['%video%'] = "{}%".format(str(round(type_dic['video'] / sum_type, 2)))

        # 获取广告主的十大热门文案详情
        seo_data = get_top_10_text(seo_data, advertiser_domain)

        # 计算广告主的投放渠道占比
        for i in range(5):
            number = i + 1
            seo_data['%network_imp{}%'.format(str(number))] = ""
            seo_data['%network_weight{}%'.format(str(number))] = ""
        category_buckets = response['aggregations']['platform_terms']['buckets']
        sum_category = 0
        for bucket in category_buckets:
            sum_category += bucket['doc_count']
        # 根据category的数量遍历获取，获取不超过5个
        size = len(category_buckets) if len(category_buckets) <= 5 else 5
        for i in range(size):
            number = i + 1
            bucket = category_buckets[i]
            if bucket['key'] in CHANNEL.ALL_PLATFORM:
                seo_data['%network_imp{}%'.format(str(number))] = CHANNEL.ALL_PLATFORM[int(bucket['key'])]
            seo_data['%network_weight{}%'.format(str(number))] = "{}%".format(
                str(round(bucket['doc_count'] / sum_category, 2)))

        # 广告主的top3 热门素材分析
        seo_data = get_top_3_heat_creative(seo_data, response)

        seo_content = json.dumps({
            "index": sort_number,
            "template": "ac_template",
            "url_route": advertiser_domain,
            "placeholders": seo_data
        }, cls=DecimalEncoder)
        # 存储到文件中
        filename = (SAVE_DIRECTORY + 'sort/{}.json').format(str(sort_number))
        with open(filename, 'w') as f:
            f.write(seo_content)


def get_top_10_text(seo_data, advertiser_domain):
    # 初始化
    for i in range(10):
        number = i + 1
        seo_data["%text{}_title%".format(str(number))] = ""
        seo_data["%text{}_group%".format(str(number))] = ""
        seo_data["%text{}_categories%".format(str(number))] = ""
    # 计算广告主的十大入门文案
    body = {
        "size": 0,
        "track_total_hits": True,
        "query": get_common_query(advertiser_domain),
        "aggs": {
            "text_nested": {
                "nested": {
                    "path": "text_groups"
                },
                "aggs": {
                    "text_aggs": {
                        "terms": {
                            "field": "text_groups.text_md5",
                            "size": 10
                        },
                        "aggs": {
                            "text_reverse": {
                                "reverse_nested": {},
                                "aggs": {
                                    "sum_creative": {
                                        "sum": {
                                            "field": "creative_group_count"
                                        }
                                    }
                                }
                            },
                            "aggs_hits": {
                                "top_hits": {
                                    "size": 1,
                                    "_source": {
                                        "includes": ["text_groups.text_type", "text_groups.title"]
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    response = ES.search(index=ES_INDEX, body=body, request_timeout=TIMEOUT)
    buckets = response['aggregations']['text_nested']['text_aggs']['buckets']
    number = 1
    for bucket in buckets:
        seo_data["%text{}_title%".format(str(number))] = bucket['aggs_hits']['hits']['hits'][0]['_source']['title']
        seo_data["%text{}_group%".format(str(number))] = bucket['aggs_hits']['hits']['hits'][0]['_source']['text_type']
        seo_data["%text{}_categories%".format(str(number))] = bucket['text_reverse']['sum_creative']['value']
        number += 1
    return seo_data


def get_top_3_heat_creative(seo_data, response):
    # 初始化
    for i in range(3):
        number = i + 1
        seo_data["%creative_text{}%".format(str(number))] = ""
        seo_data["%creatives{}%".format(str(number))] = ""
        seo_data["%creative_network{}%".format(str(number))] = ""
        seo_data["%creative_period{}%".format(str(number))] = ""
        seo_data["%creative_categories{}%".format(str(number))] = ""
        seo_data["%creative_size{}%".format(str(number))] = ""
        seo_data["%creative_days{}%".format(str(number))] = ""
        seo_data["%creative_groups{}%".format(str(number))] = ""
        seo_data["%creative_exposure{}%".format(str(number))] = ""
        seo_data["%creative_popularity{}%".format(str(number))] = ""
    hit_data = response['hit']['hit']
    number = 1
    for data in hit_data:
        source = data['_source']
        # 素材第一个文案
        seo_data["%creative_text{}%".format(str(number))] = source['text_groups'][0]['title']
        # 素材的地址
        seo_data["%creatives{}%".format(str(number))] = json.loads(source['resources'])[0]
        # 素材投放的平台
        if int(source['platforms']) in CHANNEL.ALL_PLATFORM:
            seo_data["%creative_network{}%".format(str(number))] = CHANNEL.ALL_PLATFORM[int(source['platforms'])]
        # 素材投放的时间区间
        seo_data["%creative_period{}%".format(str(number))] = "{}~{}".format(
            datetime.datetime.fromtimestamp(source['created_at']),
            datetime.datetime.fromtimestamp(source['updated_at']))
        # 文案的类型
        seo_data["%creative_categories{}%".format(str(number))] = "视频" if source['type'] == 2 else "图片"
        # 素材尺寸
        seo_data["%creative_size{}%".format(str(number))] = source['preview_img_size']
        # 素材投放天数
        seo_data["%creative_days{}%".format(str(number))] = source['days']
        # 素材创意组数
        seo_data["%creative_groups{}%".format(str(number))] = source['creative_group_count']
        # 素材展现预估
        seo_data["%creative_exposure{}%".format(str(number))] = source['impression']
        # 素材热度
        seo_data["%creative_popularity{}%".format(str(number))] = source['heat']
        number += 1
    return seo_data


def get_common_query(advertiser_domain):
    """
    获取公共的query条件
    @param advertiser_domain:
    @return:
    """
    return {
        "bool": {
            "must": [
                {
                    "term": {
                        "is_deleted": 0
                    }
                },
                {
                    "nested": {
                        "path": "advertisers",
                        "query": {
                            "bool": {
                                "must": [
                                    {
                                        "term": {
                                            "advertisers.domain": advertiser_domain
                                        }
                                    }
                                ]
                            }
                        }
                    }
                },
            ]
        },
        "must_not": [
            {
                "term": {
                    "type": {
                        "value": 0
                    }
                }
            },
            {
                "term": {
                    "type": {
                        "value": 5
                    }
                }
            }
        ]
    }


def get_array_form_buckets(buckets, style):
    """
    根据style和id获取具体的名称
    @param buckets:
    @param style:
    @return:
    """
    array = []
    for bucket in buckets:
        key = int(bucket['key'])
        # 获取id对应的平台名称
        if style == "platform" and int(key) in CHANNEL.ALL_PLATFORM:
            array.append(CHANNEL.ALL_PLATFORM[int(key)])
        # 获取id对应的分类名称
        elif style == 'category':
            for item in CATEGORY.ALL_ITEMS.keys():
                if key in item:
                    array.append(CATEGORY.ALL_ITEMS[item]['zh-CN'])
        # 获取id对应的主题名称
        elif style == 'theme' and key in THEME.ALL_ITEMS:
            array.append(THEME.ALL_ITEMS[key])
    return json.dumps(array)


def to_better(name):
    """
    去除数据中的特殊字符，将所有字母小写
    :param name:
    :return:
    """
    return re.sub(r'\W+', '-', name).replace("_", '-').strip('-').lower()


class DecimalEncoder(json.JSONEncoder):
    """
    json.dumps()方法转换decimal数据
    """

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        return super(DecimalEncoder, self).default(obj)
