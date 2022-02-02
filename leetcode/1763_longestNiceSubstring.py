class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_len = 0
        end = 0
        for i, element in enumerate(s):
            lower = 0
            upper = 0
            for j in range(i, len(s)):
                each = s[j]
                if each.islower():
                    lower |= 1 << (ord(each) - ord('a'))
                if each.isupper():
                    upper |= 1 << (ord(each) - ord('A'))

                if upper == lower and j - i + 1 > max_len:
                    max_len = j - i + 1
                    end = j
        return s[end - max_len + 1: end + 1]


s = Solution()
print(s.longestNiceSubstring('YazaAay'))
