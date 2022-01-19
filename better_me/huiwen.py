#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2021/11/24 9:59 上午 
# @Author  : kuangchao@zingfront.com
# @File    : huiwen.py
# @Description :
import sys


def getNum(s):

    n_list = [[True] * (len(s) + 1) for _ in range(len(s) + 1)]
    ans = 0
    best = s[0]
    for j in range(2, len(s) + 1):
        for i in range(j - 1, 0, -1):

            if i == j - 1:
                n_list[i][j] = (s[i - 1] == s[j - 1])
            else:
                n_list[i][j] = (n_list[i+1][j-1]) and (s[i - 1] == s[j - 1])

            if n_list[i][j] and j - i + 1 >= ans:
                ans = j - i + 1
                best = s[i-1:j]

    return best

print(getNum('a'))