from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        使用动态规划
        """
        dp = {0: 1}
        length = len(nums)
        for i in range(1, length):
            dp[i] = 1
            for j in dp.keys():
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp.values())


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
