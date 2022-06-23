class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 0, 1
        for _ in range(n):
            cur, prev = prev + cur, cur
        return cur


s = Solution()
print(s.climbStairs(3))
print(s.climbStairs(5))
print(s.climbStairs(10))