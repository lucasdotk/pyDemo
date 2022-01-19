#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/12/28 5:20 下午 
# @Author  : kuangchao@zingfront.com
# @File    : gil_test.py
# @Description :

import threading
import asyncio

n = 0

def count():
    global n
    for i in range(1000000):
        n -= 1

def count2():
    global n
    for i in range(1000000):
        n += 1

if __name__ == "__main__":
    t1 = threading.Thread(target=count)
    t2 = threading.Thread(target=count2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(n)