from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 使用倒序的方式来填充原数组，这样不会覆盖原数组中的值
        l1, l2 = m - 1, n - 1
        for i in range(len(nums1) - 1, -1, -1):
            if l1 < 0:
                nums1[i] = nums2[l2]
                l2 -= 1
            elif l2 < 0:
                nums1[i] = nums1[l1]
                l1 -= 1
            elif nums1[l1] >= nums2[l2]:
                nums1[i] = nums1[l1]
                l1 -= 1
            else:
                nums1[i] = nums2[l2]
                l2 -= 1


s = Solution()
test = [2, 5, 6, 0, 0, 0]
s.merge(test, 3, [1, 2, 3], 3)
print(test)