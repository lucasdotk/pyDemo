#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/2/7 5:31 下午 
# @Author  : kuangchao
# @File    : 0007_reverse.py
# @Description :


class Solution:
    def reverse(self, x: int) -> int:
        max_int = ((1 << 31) - 1) // 10
        min_int = (-(1 << 31)) // 10 + 1
        """
        需要特别注意，在Python中负数//10时会进行四舍五入
        -(1 << 31))为-2147483648，而(-(1 << 31)) // 10为-214748365，末位是8导致进位
        所以需要特殊处理，将//10的数加1，达到我们预期的数字
        """
        res = 0

        while x:
            if min_int <= res <= max_int:
                digit = x % 10
                """
                同样，负数在取余时，如-123%10会是7，次数需要将7-10得到我们预期的数字
                """
                if x < 0 and digit > 0:
                    digit -= 10
                x = (x - digit) // 10
                res = res * 10 + digit
            else:
                return 0
        return res


s = Solution()
print(s.reverse(-1563847412))
