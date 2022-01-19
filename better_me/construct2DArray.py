#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/1/6 2:17 下午 
# @Author  : kuangchao@zingfront.com
# @File    : construct2DArray.py
# @Description :
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) > m * n:
            return []
        res = [[0 for _ in range(n)] for _ in range(m)]
        count = 0
        for i, data in enumerate(res):
            for j, _ in enumerate(data):
                if count >= len(original):
                    return res
                res[i][j] = original[count]
                count += 1
        return res


original = [1,2,3,4,5,6]
m, n = 2, 4
s = Solution()
print(s.construct2DArray(original,m,n))