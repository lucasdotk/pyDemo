#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/11/4 3:49 下午
# @Author  : kuangchao@zingfront.com
# @File    : interaction_data_trend.py
# @Description :

from peewee import *


class InteractionDataTrend():
    ad_key = CharField(index=True, null=True)
    app_type = IntegerField(null=True)
    bk_int = IntegerField(null=True)
    bk_string = CharField(null=True)
    comment_count = IntegerField(null=True)
    created_at = DateTimeField(null=True)
    days = IntegerField(null=True)
    first_seen = DateTimeField(null=True)
    heat_degree = IntegerField(null=True)
    is_deleted = IntegerField(null=True)
    last_seen = DateTimeField(null=True)
    like_count = IntegerField(null=True)
    platform = IntegerField(null=True)
    post_id = CharField(index=True, null=True)
    rate = FloatField(null=True)
    share_count = IntegerField(null=True)
    track_count = IntegerField(null=True)
    trend_data = TextField(null=True)
    type = IntegerField(null=True)
    updated_at = DateTimeField(null=True)

    class Meta:
        table_name = 'interaction_data_trend'
