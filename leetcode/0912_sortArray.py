import random
from typing import List


class Solution:
    """
    快速排序,时间复杂度为O(nlogn),最差会达到O(n**2),有序数组排序时交换次数非常多
    """

    count = 0

    def get_partition(self, nums: List[int], left: int, right: int):
        self.count += 1
        # 随机选取一个点来分割数组
        pivot = random.randint(left, right)
        # 交换pivot点和最右侧值
        nums[pivot], nums[right] = nums[right], nums[pivot]

        i = left
        for j in range(left, right):
            if nums[j] < nums[right]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        # i此时就是pivot对应的值应该在的位置，因为此时nums[i]左边的值都小于nums[i]，而右边的值都大于nums[i]
        return i

    def quick_sort(self, nums: List[int], left: int, right: int):
        if right - left <= 0:
            return
        i = self.get_partition(nums, left, right)
        self.quick_sort(nums, left, i - 1)
        self.quick_sort(nums, i + 1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums


s = Solution()
print(s.sortArray([3, 5, 4, 7, 2, 8, 1]))
print(s.count)
