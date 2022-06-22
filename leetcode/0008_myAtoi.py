import re


class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        MAX_INT = (1 << 31) - 1
        MIN_INT = -(1 << 31)
        flag = True
        index = 0

        # 去除前导空格
        for e in s:
            if e == " ":
                index += 1
            else:
                break

        if index == len(s):
            return 0

        # 只获取一次符号位
        if s[index] == "-":
            index += 1
            flag = False
        elif s[index] == "+":
            index += 1
            flag = True

        for e in s[index:]:
            if 48 <= ord(e) <= 57:
                res.append(e)
            else:
                break

        num = 0
        if len(res) > 0:
            num_str = "".join(res)
            num = int(num_str) if flag else -(int(num_str))

        if num > MAX_INT:
            return MAX_INT
        elif num < MIN_INT:
            return MIN_INT
        return num

    def myAtoi2(self, s: str) -> int:
        """
        使用正则表达式方案
        """
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)


s = Solution()
print(s.myAtoi("4193 with words"))
print(s.myAtoi("   +0 123"))
print(s.myAtoi("42"))
