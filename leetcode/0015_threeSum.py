import sys
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for e in nums:
            tmp = set()
            for i, ele in enumerate(nums):
                if -(ele + e) in tmp:
                    res.append([e, ele, -(ele + e)])
                else:
                    tmp.add(ele)

        return res


nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
print(s.threeSum(nums))

print(1 << 63)