#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/1/10 3:22 下午 
# @Author  : kuangchao@zingfront.com
# @File    : numDecodings.py
# @Description :
from copy import copy
from typing import Set
import cProfile
import re
import numpy


class Solution:
    def numDecodings(self, s: str) -> int:

        # 处理开始是0的情况
        if s[0] == '0':
            return 0

        elem_0, elem_1, cur = 1, 1, 1
        for i in range(1, len(s)):
            ch = s[i]
            cur = 0
            if ch != '0':
                cur += elem_1
            if int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                cur += elem_0
            elem_0, elem_1 = elem_1, cur
        return cur

    def get_str_list(self, s: str) -> Set[str]:
        if s[0] == '0':
            return set()

        more_prev = [['']]
        prev = [[s[0]]]
        cur = [[s[0]]]

        for i in range(1, len(s)):
            num = s[i]
            cur = []
            if num != '0':
                for e in prev:
                    tmp = copy(e)
                    tmp.append(num)
                    cur.append(tmp)
            if int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                for e in more_prev:
                    tmp = copy(e)
                    tmp.append(s[i - 1:i + 1])
                    cur.append(tmp)
            more_prev, prev = prev, cur
        print(cur)
        res = set()
        for e in cur:
            letter = ''
            for each in e:
                if each != '':
                    letter += chr(int(each) + 96)
            res.add(letter)
        return res


def get_str_list(s: str) -> Set[str]:
    if s[0] == '0':
        return set()

    more_prev = [['']]
    prev = [[s[0]]]
    cur = [[s[0]]]

    for i in range(1, len(s)):
        num = s[i]
        cur = []
        if num != '0':
            for e in prev:
                tmp = copy(e)
                tmp.append(num)
                cur.append(tmp)
        if int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
            for e in more_prev:
                tmp = copy(e)
                tmp.append(s[i - 1:i + 1])
                cur.append(tmp)
        more_prev, prev = prev, cur
    print(cur)
    res = set()
    for e in cur:
        letter = ''
        for each in e:
            if each != '':
                letter += chr(int(each) + 96)
        res.add(letter)
    return res


so = Solution()
print(so.get_str_list('1231201023'))
# cProfile.run('re.compile("get_str_list|1231201023")')
print(numpy.arange(100))
