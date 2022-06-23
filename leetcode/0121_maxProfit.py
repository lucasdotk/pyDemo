from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = int(1e4)
        max_benefit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_benefit:
                max_benefit = p - min_price

        return max_benefit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
