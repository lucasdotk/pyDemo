from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        ans = 0
        for ele in rectangles:
            min_value = min(ele[0], ele[1])
            if min_value > ans:
                ans = min_value
                count = 1
                continue

            if min_value == ans:
                count += 1

        return count


s = Solution()
print(s.countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
