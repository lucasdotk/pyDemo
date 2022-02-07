#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/2/7 10:09 上午 
# @Author  : lucas
# @File    : 1405_longestDiverseString.py
# @Description :

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        str_list = [['a', a], ['b', b], ['c', c]]
        res = []

        while True:
            str_list = sorted(str_list, key=lambda ele: -ele[1])
            has_next = False

            for i, (ch, num) in enumerate(str_list):
                if num <= 0:
                    break
                if len(res) >= 2 and res[-2] == ch and res[-1] == ch:
                    continue

                has_next = True
                res.append(ch)
                str_list[i][1] -= 1
                break

            if not has_next:
                return "".join(res)


a = 1
b = 1
c = 7
s = Solution()
print(s.longestDiverseString(a, b, c))
