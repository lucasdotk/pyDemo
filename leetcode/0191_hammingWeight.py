class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        每一位和1做与运算，时间复杂度为O(k)
        """
        num, res = 1, 0
        for _ in range(32):
            if num & n:
                res += 1
            num <<= 1
        return res

    def hammingWeight2(self, n: int) -> int:
        """
        利用n&(n-1)会将n最后一位的1置位0的特性，时间复杂度为O(log n),其中n最大为32
        """
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res


s = Solution()
print(s.hammingWeight(-3))
print(s.hammingWeight2(7))
number = -3 % (1 << 32)
print(s.hammingWeight2(number))
