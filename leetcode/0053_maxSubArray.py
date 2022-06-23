from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        使用动态规划，f(i)=max{f(i−1)+nums[i],nums[i]}
        @param nums:
        @return:
        """
        res, prev = nums[0], 0
        for num in nums:
            prev = max(num + prev, num)
            res = max(res, prev)

        return res


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
