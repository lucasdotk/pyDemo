import sys
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total_left_size = (m + n + 1) // 2

        left = 0
        right = m

        # 找到符合条件的left位置
        while left < right:
            # 在短数组中的位置
            i = (left + right + 1) // 2
            # 在长数组中的位置
            j = total_left_size - i

            if nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                left = i

        # 短数组中的分割线位置
        i = left
        # 长数组的分割线位置
        j = total_left_size - left

        min_nums1_left = nums1[i - 1] if i > 0 else -(1 << 32)
        min_nums2_left = nums2[j - 1] if j > 0 else -(1 << 32)
        max_nums1_right = nums1[i] if i < m else sys.maxsize
        max_nums2_right = nums2[j] if j < n else sys.maxsize

        if (m + n) % 2 == 0:
            return (min(max_nums1_right, max_nums2_right) + max(min_nums1_left, min_nums2_left)) / 2
        else:
            return max(min_nums1_left, min_nums2_left)


a = [1, 2, 3, 5, 7, 8]
b = [3, 6, 7, 8, 9, 10]
s = Solution()
print(s.findMedianSortedArrays(a, b))

a = [1, 2, 3, 5, 7, 8, 9]
b = [3, 6, 7, 8, 9, 10]
print(s.findMedianSortedArrays(a, b))