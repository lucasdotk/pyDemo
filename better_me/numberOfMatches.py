#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/1/25 4:58 下午 
# @Author  : kuangchao@zingfront.com
# @File    : numberOfMatches.py
# @Description :


class Solution:
    def numberOfMatches(self, n: int) -> int:
        times = 0
        while True:
            fight = n // 2
            n = fight + n % 2
            times += fight
            if n < 2:
                break
        return times


s = Solution()
print(s.numberOfMatches(1))
