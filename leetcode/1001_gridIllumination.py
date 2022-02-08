#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/2/8 4:07 下午 
# @Author  : kuangchao
# @File    : 1001_.py
# @Description :
from typing import List
import collections


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for q in queries:
            find = False
            x, y = q[0], q[1]
            for lamp in lamps:
                if x == lamp[0] or y == lamp[1] or x + y == lamp[0] + lamp[1] or x - y == lamp[0] - lamp[1]:
                    find = True
                    res.append(1)
                    break
            if not find:
                res.append(0)

            # 关灯
            close_light = []
            for i, lamp in enumerate(lamps):
                for now_x, now_y in [(x, y), (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1), (x - 1, y - 1),
                                     (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]:
                    if 0 <= now_x < n and 0 <= now_y < n and now_x == lamp[0] and now_y == lamp[1]:
                        close_light.append(i)
            tmp = []
            for i in range(len(lamps)):
                if i not in close_light:
                    tmp.append(lamps[i])
            lamps = tmp
        return res

    def gridIllumination_1(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        使用hashSet提升性能，通过hashMap记录每种规则的次数（两个灯可能包含部分相同的规则）
        :param n:
        :param lamps:
        :param queries:
        :return:
        """
        l_set = set()
        x_dict, y_dict, line_dict, anti_line_dict = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
        """
        Counter()是字典的子类，用于计数非常方便
        方便之处1：
        如a = {};a['a'] +=1;此时会提示我们字典a里面没有'a'
        而使用a = Counter();a['a'] +=1;就没有问题
        
        方便之处2：
        如a = {};print(a['a']);此时会提示我们keyError，字典里不存在此元素
        而使用a = Counter();print(a['a']);会返回0，这样易于我们知道元素是否在字典中
        """
        for x, y in lamps:
            if (x, y) not in l_set:
                l_set.add((x, y))
                x_dict[x] += 1
                y_dict[y] += 1
                line_dict[x + y] += 1
                anti_line_dict[x - y] += 1

        res = [0] * len(queries)
        for i, (now_x, now_y) in enumerate(queries):
            if x_dict[now_x] or y_dict[now_y] or line_dict[now_x + now_y] or anti_line_dict[now_x - now_y]:
                res[i] = 1

            for cur_x in range(now_x - 1, now_x + 2):
                for cur_y in range(now_y - 1, now_y + 2):
                    if 0 <= cur_x < n and 0 <= cur_y < n and (cur_x, cur_y) in l_set:
                        l_set.remove((cur_x, cur_y))
                        x_dict[cur_x] -= 1
                        y_dict[cur_y] -= 1
                        line_dict[cur_x + cur_y] -= 1
                        anti_line_dict[cur_x - cur_y] -= 1

        return res


so = Solution()
n = 6
lamps = [[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]]
queries = [[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]]
print(so.gridIllumination(n, lamps, queries))
print(so.gridIllumination_1(n, lamps, queries))
