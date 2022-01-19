#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/12/28 11:23 上午 
# @Author  : kuangchao@zingfront.com
# @File    : demo.py
# @Description :
from functools import reduce


def fibonacci():
    n, i, j = 0, 0, 1
    while True:
        yield j
        i, j = j, i + j
        n += 1


def x(n):
    f = fibonacci()
    for _ in range(n):
        print(f.__next__())


x(6)


def triangle(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    res = [1, 1]
    for i in range(n - 2):
        tmp = [1]
        for j in range(len(res) - 1):
            tmp.append(res[j] + res[j + 1])
        tmp.append(1)
        res = tmp
    return res


def g_triangle():
    res = [1]
    while True:
        yield res
        if len(res) >= 2:
            tmp = [1]
            for i in range(len(res) - 1):
                tmp.append(res[i] + res[i + 1])
            res = tmp
        res.append(1)


g_t = g_triangle()
for _ in range(10):
    print(g_t.__next__())


def func(n):
    yield n *2

g = func(5)
print(g.__next__())

for i in g:
    print("hh")
    print(i)


numList = [1,2,3,4,5]

sum = sum(numList)  #sum = 15
maxNum = max(numList) #maxNum = 5
minNum = min(numList) #minNum = 1
from operator import mul
prod = reduce(mul, numList, 1) #prod = 120 默认值传1以防空列表报错
print(prod)