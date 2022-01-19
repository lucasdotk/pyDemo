#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2020年04月10日 21:39:00
# @Author   : liliangqing
# @File     : es_util.py
# @description : 根据机器选择ES地址

import socket
from elasticsearch import Elasticsearch

ES_TIMEOUT = 600

# 北京内网
ES_BJ_INNERNET = Elasticsearch([{
    'host': 'es-cn-n6w1qdk0f000bp3w8.elasticsearch.aliyuncs.com',
    'port': 9200,
    'http_auth': ('elastic', 'ES_bj@common1423'),
    'use_ssl': False
}], timeout=ES_TIMEOUT)
# 北京外网
ES_BJ_OUTNET = Elasticsearch([{
    'host': 'es-cn-n6w1qdk0f000bp3w8.public.elasticsearch.aliyuncs.com',
    'port': 9200,
    'http_auth': ('elastic', 'ES_bj@common1423'),
    'use_ssl': False
}], timeout=ES_TIMEOUT)
# 美国内网
ES_US_INNERNET = Elasticsearch([{
    'host': 'es-cn-6ja1pcr6x000nzc15.elasticsearch.aliyuncs.com',
    'port': 9200,
    'http_auth': ('elastic', 'ES@common_us0619'),
    'use_ssl': False
}], timeout=ES_TIMEOUT)
# 美国外网
ES_US_OUTNET = Elasticsearch([{
    'host': 'es-cn-6ja1pcr6x000nzc15.public.elasticsearch.aliyuncs.com',
    'port': 9200,
    'http_auth': ('elastic', 'ES@common_us0619'),
    'use_ssl': False
}], timeout=ES_TIMEOUT)


# 根据节点获取ES point(1:北京节点 2:美国节点)
def get_es(point=1):
    machine = 'us'
    hostname = socket.gethostname()

    if hostname:
        names = hostname.split(".")

        if names[0] == 'bj':
            machine = 'bj'

    if point == 1:
        if machine == 'bj':
            ES = ES_BJ_INNERNET
        else:
            ES = ES_BJ_OUTNET
    else:
        if machine == 'us':
            ES = ES_US_INNERNET
        else:
            ES = ES_US_OUTNET

    return ES
