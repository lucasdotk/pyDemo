#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/1/24 2:57 下午 
# @Author  : kuangchao@zingfront.com
# @File    : connect_redis.py
# @Description :

import redis

r = redis.Redis(host='r-rj9kc7ks1dlww7ude7.redis.rds.aliyuncs.com', db=3, port=6379, decode_responses=True, password='Slb@zf0311')

res = []
cursor = 0
while True:
    data = r.scan(cursor)
    cursor = data[0]
    for ele in data[1]:
        if ':' not in ele:
            res.append(ele)

    print(cursor)

    if cursor == 0:
        break

print(res)