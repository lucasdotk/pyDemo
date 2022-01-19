#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/1/6 2:51 下午 
# @Author  : kuangchao@zingfront.com
# @File    : lastRemaining.py
# @Description :


class Solution:
    def lastRemaining(self, n: int) -> int:
        e_list = [i + 1 for i in range(n)]
        while len(e_list) > 1:
            tmp = []
            for i in range(1, len(e_list), 2):
                tmp.append(e_list[i])
            e_list = [tmp[len(tmp) - i - 1] for i in range(len(tmp))]
        return e_list[0]

s = Solution()
print(s.lastRemaining(8))

