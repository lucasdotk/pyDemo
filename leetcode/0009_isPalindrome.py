class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ele = str(x)
        n = len(ele)
        if n % 2 == 0:
            left = n // 2 - 1
            right = n // 2
        else:
            left = n // 2 - 1
            right = n // 2 + 1

        while left >= 0:
            if ele[left] != ele[right]:
                return False
            left -= 1
            right += 1
        return True

    def isPalindrome_1(self, x: int) -> bool:
        """
        直接翻转字符串
        @param x:
        @return:
        """
        return x > -1 and str(x)[::-1] == str(x)

    def isPalindrome_2(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        half = 0
        while x > half:
            half = half * 10 + x % 10
            x = x // 10

        return half == x or half // 10 == x


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome_2(121))