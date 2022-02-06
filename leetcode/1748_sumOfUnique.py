#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        tmp = {}
        for num in nums:
            if num not in tmp:
                tmp[num] = 1
            else:
                tmp[num] += 1

        res = 0
        for k, v in tmp.items():
            if v == 1:
                res += k
        return res

    def sumOfUnique_1(self, nums: List[int]) -> int:
        tmp = Counter(nums)
        res = 0
        for k, v in tmp.items():
            if v == 1:
                res += k
        return res


s = Solution()
print(s.sumOfUnique([1, 2, 3, 2]))
print(s.sumOfUnique_1([1, 2, 3, 2]))
