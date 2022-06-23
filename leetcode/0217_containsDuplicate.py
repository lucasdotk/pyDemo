from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        if len(num_set) < len(nums):
            return True
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        """
        速度最快
        """
        num_set = set()
        for i, num in enumerate(nums):
            num_set.add(num)
            if i + 1 > len(num_set):
                return True
        return False

    def containsDuplicate3(self, nums: List[int]) -> bool:
        num_map = {}
        for num in nums:
            if num in num_map:
                return True
            num_map[num] = 1
        return False


s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
print(s.containsDuplicate2([1, 2, 3, 1]))
print(s.containsDuplicate3([1, 2, 3, 1]))
