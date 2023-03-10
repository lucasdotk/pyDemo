from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while end - start > 1:
            pivot = int((start + end) / 2)
            if nums[end] > nums[pivot]:
                end = pivot
            else:
                start = pivot
        return min(nums[start], nums[end])

    def findMin2(self, nums: List[int]) -> int:
        """
        官方解法
        @param nums:
        @return:
        """
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([11, 13, 15, 17]))
print(s.findMin([1]))
print(s.findMin([2, 1]))
print(s.findMin([2, 3, 4, 5, 1]))
