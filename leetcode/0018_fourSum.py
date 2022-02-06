#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/2/6 6:57 下午 
# @Author  : lucas
# @File    : 0018_fourSum.py
# @Description :
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i + 1, n):
                right = n - 1
                for k in range(j + 1, n):
                    now = nums[i] + nums[j] + nums[k]
                    while now + nums[right] > target and right > k:
                        right -= 1
                    if now + nums[right] == target:
                        res.append([nums[i], nums[j], nums[k], nums[right]])
        return res


s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(s.fourSum(nums, target))
