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
        for i in range(n - 3):
            # 防止重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 对于一定不能成立的结果跳过
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                # 防止重复
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue

                # 对于一定不能成立的结果跳过
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                right = n - 1
                for k in range(j + 1, n - 1):
                    # 防止重复
                    if k - 1 > j and nums[k] == nums[k - 1]:
                        continue
                    now = nums[i] + nums[j] + nums[k]
                    while now + nums[right] > target and right > k:
                        right -= 1
                    if now + nums[right] == target and right != k:
                        res.append([nums[i], nums[j], nums[k], nums[right]])
        return res


s = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(s.fourSum(nums, target))
