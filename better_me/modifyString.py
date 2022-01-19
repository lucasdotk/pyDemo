#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/1/5 1:59 下午 
# @Author  : kuangchao@zingfront.com
# @File    : modifyString.py
# @Description :


class Solution:


    def modifyString(self, s: str) -> str:
        elem_list = ['a', 'b', 'c']
        new_s_list = []
        prev = ""
        for i, elem in enumerate(s):
            if elem == "?":
                nxt = ""
                if i + 1 < len(s):
                    nxt = s[i + 1]
                for e in elem_list:
                    if e not in [prev, nxt]:
                        new_s_list.append(e)
                        prev = e
                        break
            else:
                new_s_list.append(elem)
                prev = elem
        return "".join(new_s_list)


# elem_list = list(map(lambda i: chr(i), range(ord('a'), ord('a') + 26)))
#
# elem_list_1 = [chr(i) for i in range(ord('z'), ord('a') - 1, -1)]


s = Solution()
print(s.modifyString('sf????f???'))
