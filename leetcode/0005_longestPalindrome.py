class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(left: int, right: int):

            if left < 0 or right >= len(s):
                return False

            if s[left] == s[right]:
                return True
            return False

        def get_max_string(left: int, right: int, ele: str):
            while True:
                if is_palindrome(left, right):
                    ele = s[left:right + 1]
                    left -= 1
                    right += 1
                    continue
                break
            return ele

        max_s = ''
        for i, e in enumerate(s):
            tmp_l = get_max_string(i, i, e)
            tmp_r = get_max_string(i, i + 1, e)
            tmp = tmp_l if len(tmp_l) > len(tmp_r) else tmp_r
            if len(tmp) > len(max_s):
                max_s = tmp
        return max_s


so = Solution()
print(so.longestPalindrome('werref'))
