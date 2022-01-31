class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            count += 1

        return count

    def numberOfSteps_1(self, num: int) -> int:
        count = 0
        while num:
            count += (1 & num)
            if num > 1:
                count += 1
            num >>= 1

        return count


s = Solution()
print(s.numberOfSteps(14))

print(15 & 1)