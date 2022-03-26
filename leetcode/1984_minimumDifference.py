#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/2/11 2:50 下午 
# @Author  : kuangchao
# @File    : 1984_minimumDifference.py
# @Description :
import sys
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return 0

        nums.sort(reverse=True)
        end = k - 1
        res = sys.maxsize
        for num in nums[:len(nums) - k + 1]:
            if num - nums[end] < res:
                res = num - nums[end]
            end += 1
        return res

    def minimumDifference_1(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))


so = Solution()
nums = [9, 4, 1, 7]
k = 2
print(so.minimumDifference(nums, k))
