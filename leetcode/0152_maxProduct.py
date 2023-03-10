from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        使用动态规划，其中因为负负得正的乘法特性，故维护一个min_num，这个值为负值时，在遇到一个负值后可能成为最大值
        @param nums:
        @return:
        """
        res, max_num, min_num = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            # 保留max_num的值，用于min_num的计算
            max_num_tmp = max_num
            max_num = max(max_num * num, min_num * num, num)
            min_num = min(min_num * num, max_num_tmp * num, num)
            res = max(max_num, res)

        return res


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))
print(s.maxProduct([-2, 0, -1]))
print(s.maxProduct([-3, -1, -1]))
print(s.maxProduct([-2, 3, -4]))
print(s.maxProduct([-4, -3, -2]))
