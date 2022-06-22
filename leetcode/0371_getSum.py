class Solution:
    def getSum(self, a: int, b: int) -> int:
        MUSK1 = 1 << 32
        MUSK2 = 1 << 31
        # MUSK3 = 2147483647  # (1 << 31) - 1
        MUSK3 = 4294967295  # (1 << 32) - 1

        # 将所有超过32位的数 置为0
        a = a % MUSK1
        b = b % MUSK1

        while b != 0:
            carry = ((a & b) << 1) % MUSK1
            a = (a ^ b) % MUSK1
            b = carry

        if a & MUSK2:
            return ~ (a ^ MUSK3)
        return a


s = Solution()
print(s.getSum(2, 3))
print(s.getSum(2, -3))
print(s.getSum(-2, 3))
print(s.getSum(-2, -3))
