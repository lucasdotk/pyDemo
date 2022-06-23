from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        best_list = [0] * (amount + 1)
        for i in range(1, amount + 1):
            for j in coins:
                if j <= i:
                    # 处理所有货币都无法构成i金额的情况
                    if i != j and best_list[i - j] == 0:
                        continue

                    if best_list[i] != 0:
                        best_list[i] = min(best_list[i], best_list[i - j] + 1)
                    else:
                        best_list[i] = best_list[i - j] + 1

        if best_list[amount] == 0:
            return -1
        return best_list[amount]

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """
        优化在于使用coin列表作为外层循环，去除一些无用的金额循环
        """
        if amount == 0:
            return 0

        best_list = [0] * (amount + 1)
        for i in coins:
            for j in range(i, amount + 1):
                # 处理所有货币都无法构成i金额的情况
                if i != j and best_list[j - i] == 0:
                    continue

                if best_list[j] != 0:
                    best_list[j] = min(best_list[j], best_list[j - i] + 1)
                else:
                    best_list[j] = best_list[j - i] + 1

        if best_list[amount] == 0:
            return -1
        return best_list[amount]

    def coinChange3(self, coins: List[int], amount: int) -> int:
        """
        代码更简洁，使用了float('inf')即无穷大，任何数与他比较都是小于此数
        """
        best_list = [float('inf')] * (amount + 1)
        best_list[0] = 0
        for i in coins:
            for j in range(i, amount + 1):
                best_list[j] = min(best_list[j], best_list[j - i] + 1)

        if best_list[amount] == float('inf'):
            return -1
        return best_list[amount]


s = Solution()
print(s.coinChange([1, 2, 5], 7))
print(s.coinChange([5], 1))
print(s.coinChange([1, 2, 5], 0))
print(s.coinChange([2], 3))

print(s.coinChange2([1, 2, 5], 7))
print(s.coinChange2([5], 1))
print(s.coinChange2([1, 2, 5], 0))
print(s.coinChange2([2], 3))

print(s.coinChange3([1, 2, 5], 7))
print(s.coinChange3([5], 1))
print(s.coinChange3([1, 2, 5], 0))
print(s.coinChange3([2], 3))
