#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/1/10 2:59 下午 
# @Author  : kuangchao@zingfront.com
# @File    : decompressRLElist.py
# @Description :
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        x = 0
        for i,num in enumerate(nums):
            if i % 2 == 0:
                x = num
            if i % 2 == 1:
                res.extend(list(map(lambda _: num, range(x))))
        return res

s = Solution()
print(s.decompressRLElist([1,2,3,4]))