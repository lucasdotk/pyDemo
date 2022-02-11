#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/2/9 9:50 上午 
# @Author  : kuangchao
# @File    : 2006_countKDifference.py
# @Description :
import collections
from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i, num in enumerate(nums[:n - 1]):
            for j in range(i + 1, n):
                e = nums[j]
                if num - e == k or e - num == k:
                    res += 1
        return res

    def countKDifference_1(self, nums: List[int], k: int) -> int:
        """
        使用hash表来提升性能，因为不需要输出那些数字组成了结果，所有value中存储数字在数组中出现的次数
        :param nums:
        :param k:
        :return:
        """
        n_dict = collections.Counter()
        res = 0
        for num in nums:
            res += n_dict[num - k] + n_dict[num + k]
            n_dict[num] += 1
        return res


so = Solution()
print(so.countKDifference([3, 3], 2))
print(so.countKDifference_1([1, 2, 2, 1], 1))
