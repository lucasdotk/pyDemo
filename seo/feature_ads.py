#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/11/1 11:04 上午
# @Author  : kuangchao@zingfront.com
# @File    : get_feature_ads.py
# @Description :

import os
import time
import json
import datetime
import logging
from elasticsearch import Elasticsearch
from transparent_ads.interaction_data_analysis.utils import get_interaction_data_by_post, dingding_report
from api.models.sp_biz.interaction_data_trend import InteractionDataTrend

# es配置
TIMEOUT = 180
BS_ES = Elasticsearch([{
    'host': 'es-cn-tl32n4pb8000jmsla.elasticsearch.aliyuncs.com',
    'port': 9200,
    'http_auth': ('elastic', 'S$BcPucSo5'),
    'use_ssl': False
}], timeout=TIMEOUT)

# 日志配置
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)
logger = logging.getLogger('get_feature_ads')

# 精选创意文件所在目录
file_path = '/data/work/adspyhub/feature_ads'
# 记录精选创意开始追踪的开始时间，3天为一个周期
when_start_track_file = '/data/work/adspyhub/feature_ads/when_start_track.txt'


def feature_ads_analysis():
    """
    分析互动数据，获取精选创意
    @return:
    """
    # 今天日期字符串
    today_str = time.strftime('%Y-%m-%d')
    # 今天日期
    today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
    # 行业-索引对应表
    app_type_list = {
        1: 'sp_game_index',
        2: 'sp_tool_index',
        3: 'sp_eco_index'
    }
    # 首次加载，写入追踪开始时间文件
    if not os.path.exists(when_start_track_file):
        # 创建目录
        mkdir_multi_level(when_start_track_file)
        with open(when_start_track_file, 'w+') as f:
            f.write(today_str)

    with open(when_start_track_file, 'r') as f:
        when_start_track_str = f.read()
    when_start_track = datetime.datetime.strptime(when_start_track_str, "%Y-%m-%d")

    # 距离今天的天数
    days_to_now = (today - when_start_track).days

    for app_type in app_type_list:

        # 记录文件，根据索引区分不同文件夹
        es_index = app_type_list[app_type]
        record_file_name = '{}/{}/{}.json'.format(file_path, es_index, when_start_track_str)

        if days_to_now % 3 == 0:
            # 第一天，生成数据
            record_file_name = '{}/{}/{}.json'.format(file_path, es_index, today_str)
            first_day_analysis(record_file_name, app_type, es_index)
            # 更新when_start_track
            with open(when_start_track_file, 'w') as f:
                f.write(today_str)

        elif days_to_now % 3 == 1:
            # 第二天，更新数据
            second_day_analysis(record_file_name)

        elif days_to_now % 3 == 2:
            # 第三天，筛选数据
            third_day_analysis(record_file_name, app_type)
    return True


def first_day_analysis(record_file_name, app_type, es_index):
    """
    第一天要做的事：获取过去3天的post数据，获取互动数据，记录到文件中
    @param record_file_name:
    @param app_type:
    @param es_index:
    @return:
    """
    # 今天0点的日期和时间戳
    today_str = time.strftime('%Y%m%d')
    today_timestamp = int(time.mktime(time.strptime(today_str, "%Y%m%d")))

    body = {
        "size": 5000,
        "sort": [
            {
                "like_count": {
                    "order": "desc"
                }
            }
        ],
        "query": {
            "bool": {
                "must": [
                    {
                        "exists": {
                            "field": "like_count"
                        }
                    },
                    {
                        "exists": {
                            "field": "comment_count"
                        }
                    },
                    {
                        "exists": {
                            "field": "share_count"
                        }
                    },
                    {
                        "bool": {
                            "filter": {
                                "script": {
                                    "script": "doc['like_count'].value+doc['comment_count'].value+doc['share_count'].value > 10"
                                }
                            }
                        }
                    },
                    {
                        "term": {
                            "platform": {
                                "value": 2
                            }
                        }
                    },
                    {
                        "term": {
                            "post": {
                                "value": 1
                            }
                        }
                    },
                    {
                        "range": {
                            "created_at": {
                                "gte": today_timestamp - 86400 * 3,
                                "lt": today_timestamp
                            }
                        }
                    },
                    {
                        "term": {
                            "app_type": {
                                "value": app_type
                            }
                        }
                    }
                ]
            }
        }
    }
    response = BS_ES.search(body=body, index=es_index)

    # 获取post_id列表
    post_id_ad_key_map = {}
    for hit in response['hits']['hits']:
        source = hit['_source']
        if 'page_id' in source and 'post_id' in source and source['page_id'] and source['post_id']:
            fb_post_id = source['page_id'] + '_' + source['post_id']
            post_id_ad_key_map[fb_post_id] = hit['_id']

    # 查询graph Api获取互动数据
    post_id_list = list(post_id_ad_key_map.keys())
    interaction_data = get_interaction_data_by_post(post_id_list)

    # 记录创意key至数据中
    for post_id in interaction_data:
        interaction_data[post_id]['ad_key'] = post_id_ad_key_map[post_id]

    # 记录至文件中
    if not os.path.exists(record_file_name):
        mkdir_multi_level(record_file_name)
    with open(record_file_name, 'w+') as f:
        f.write(json.dumps(interaction_data))

    logger.info("第一天任务执行完成")
    return True


def second_day_analysis(record_file_name):
    """
    第二天要做的事，更新文件中所有post的互动数据
    @param record_file_name:
    @return:
    """
    # 更新今日的post数据
    update_post_data(record_file_name)
    logger.info("第二天任务执行完成")
    return True


def third_day_analysis(record_file_name, app_type):
    """
    第三天，更新post的互动数据，并生成精选创意
    @param record_file_name:
    @param app_type:
    @return:
    """
    # 更新今日的post数据
    interaction_data = update_post_data(record_file_name)

    # 今天日期字符串
    today_str = time.strftime('%Y%m%d')
    three_days_ago = (datetime.datetime.now() + datetime.timedelta(days=-2)).strftime("%Y%m%d")

    # 取出top30
    first_day_interaction_data = {}
    third_day_interaction_data = {}
    for post_id in interaction_data:
        data = interaction_data[post_id]
        if today_str in data and three_days_ago in data:
            if 'like' in data[today_str] and 'comment' in data[today_str] and 'share' in data[today_str]:
                third_day_interaction_data[post_id] = \
                    data[today_str]['like'] + data[today_str]['comment'] + data[today_str]['share']
            if 'like' in data[three_days_ago] and 'comment' in data[three_days_ago] and 'share' in data[three_days_ago]:
                first_day_interaction_data[post_id] = \
                    data[three_days_ago]['like'] + data[three_days_ago]['comment'] + data[three_days_ago]['share']
        else:
            logger.warning("post_id为{}的缺少第一天或第三天的数据".format(post_id))

    # 计算增长率
    rate_list = {}
    for key in first_day_interaction_data:
        if key in third_day_interaction_data:
            #like+comment+share大于100的数据
            if third_day_interaction_data[key] >= 100:
                rate = round(
                    (third_day_interaction_data[key] - first_day_interaction_data[key]) / first_day_interaction_data[
                        key] * 100, 2) if first_day_interaction_data[key] != 0 else 0
                rate_list[key] = rate

    # 取出top 30的post
    top_30_highest_rage = 0
    top_30_lowest_rate = 0
    top_30_post = {}
    rate_tuple = sorted(rate_list.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for data in rate_tuple:
        #原每次生成最多30条精选广告数据，现修改为1000条
        if len(top_30_post) < 1000:
            top_30_post[data[0]] = data[1]
            if top_30_highest_rage == 0:
                top_30_highest_rage = data[1]
            top_30_lowest_rate = data[1]

    # 将top30数据存入数据库
    for post_id in top_30_post:
        if post_id in interaction_data and 'ad_key' in interaction_data[post_id]:
            ad_key = interaction_data[post_id]['ad_key']

            # 是否有重复数据
            duplicate = InteractionDataTrend.select().where(
                InteractionDataTrend.type == 1,
                #InteractionDataTrend.is_deleted == 0,
                InteractionDataTrend.ad_key == ad_key
            ).limit(1)
            #_id重复处理
            if duplicate:
                duplicate = duplicate[0]
                if  duplicate.is_deleted == 0:
                    continue
                else:
                    #标记删除改为未删除
                    duplicate.is_deleted = 0
                    duplicate.save()
                    continue
            #post_id 重复处理
            duplicate = InteractionDataTrend.select().where(
                InteractionDataTrend.type == 1,
                #InteractionDataTrend.is_deleted == 0,
                InteractionDataTrend.post_id == post_id
            ).limit(1)
            #_id重复处理
            if duplicate:
                continue
            # 整理数据
            interaction_data_trend = InteractionDataTrend()
            interaction_data_trend.ad_key = ad_key
            interaction_data_trend.post_id = post_id
            # 1为feature Ads，2位用户添加
            interaction_data_trend.type = 1
            interaction_data_trend.app_type = app_type
            interaction_data_trend.rate = top_30_post[post_id]
            interaction_data_trend.trend_data = json.dumps(interaction_data[post_id])
            interaction_data_trend.platform = 1
            interaction_data_trend.is_deleted = 0

            # 记录至数据库中
            interaction_data_trend.save()

    # 发送钉钉消息
    title = "精选创意数据生成情况"
    content = ''
    if top_30_post:
        type_to_name = {
            1: '游戏行业',
            2: '工具行业',
            3: '电商行业'
        }
        text_title = '**{}精选创意--数据生成成功**\n\n'.format(type_to_name[app_type])
        content += "本次从近三天追踪的{}条创意中，生成了{}个精选创意；\n\n".format(str(len(interaction_data)), str(len(top_30_post)))
        content += "此批精选创意的互动数据最低增长率为{}%，最高为{}%". \
            format(str(top_30_lowest_rate), str(top_30_highest_rage))
    else:
        text_title = '**精选创意--数据生成失败**\n\n'
    text = text_title + content
    dingding_report(title, text)

    logger.info("第三天的任务执行完成")
    return True


def update_post_data(record_file_name):
    """
    每日更新post数据
    @param record_file_name:
    @return:
    """
    # 从文件中读取数据
    with open(record_file_name, 'r') as f:
        interaction_data = json.loads(f.read())

    # 更新今日的互动数据
    today_data = get_interaction_data_by_post(list(interaction_data.keys()))
    interaction_data = merge_post_data(interaction_data, today_data)

    # 记录至文件中
    with open(record_file_name, 'w') as f:
        f.write(json.dumps(interaction_data))

    return interaction_data


def merge_post_data(d1, d2):
    """
    merge两天的post数据
    @param d1:
    @param d2:
    @return:
    """
    for datum in d1:
        if datum in d2:
            d1[datum].update(d2[datum])
    return d1


def mkdir_multi_level(file_name):
    """
    创建多层目录，从第三级开始创建
    @param file_name:
    @return:
    """
    position_list = [i for i, x in enumerate(file_name) if x == '/']
    x_list = position_list[3: len(position_list)]
    for pos in x_list:
        directory_path = file_name[0: pos]
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)


if __name__ == "__main__":
    feature_ads_analysis()