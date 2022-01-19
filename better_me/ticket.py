#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/11/17 4:59 下午 
# @Author  : kuangchao@zingfront.com
# @File    : ticket.py
# @Description :


def get(prices, fee):
    # 第一天不持有的收益
    stock_0 = 0
    # 第一天持有的收益
    stock_1 = - prices[0]

    for i in range(1, len(prices)):
        tmp_0 = max(stock_0, stock_1 + prices[i] - fee)
        tmp_1 = max(stock_0 - prices[i], stock_1)

        stock_0, stock_1 = tmp_0, tmp_1

    return stock_0

print(get([1,1,1,11,3,4,5,6,77,7,4,4,4,4,0], 2))