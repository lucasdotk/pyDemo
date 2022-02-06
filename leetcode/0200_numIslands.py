#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Date    : 2022/2/6 11:34 上午 
# @Author  : lucas
# @File    : 0200_numIslands.py
# @Description :
from collections import deque
import cProfile
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        深度遍历优先
        :param grid:
        :return:
        """

        def dfs(x, y):
            grid[x][y] = '0'
            for now_x, now_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= now_x < m and 0 <= now_y < n and grid[now_x][now_y] == '1':
                    dfs(now_x, now_y)

        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res

    def numIslands_1(self, grid: List[List[str]]) -> int:
        """
        广度遍历优先
        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    q = deque()
                    q.append((i, j))

                    while q:
                        x, y = q.popleft()
                        grid[x][y] = '0'

                        """
                        在此处进行grid[x][y] = '0'时，有致命的性能缺陷
                        
                        在以下的二维数组中
                            ['1','1','1'],
                            ['1','1','1'],
                            ['1','1','1'],
                        
                        q.append((0,0))
                        q.append((0,1))
                        q.append((1,0))
                        q.append((0,2))
                        q.append((1,1))
                        q.append((1,1))  --致命的性能问题出现：重复的节点被添加了进来
                        q.append((2,0))
                        
                        虽然这种做法不会导致错误，但是会导致大量的重复添加，这些重复添加在数组长度增加时会导致严重的冗余问题
                        在一个7*20的数组中执行此程序，append的执行次数达到了400w次，正常只需要200次左右
                        """

                        for now_x, now_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                            if 0 <= now_x < m and 0 <= now_y < n and grid[now_x][now_y] == '1':
                                q.append((now_x, now_y))

        return res

    def numIslands_2(self, grid: List[List[str]]) -> int:
        """
        广度优先遍历-力扣官方答案
        :param grid:
        :return:
        """
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    neighbors = deque([(r, c)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                neighbors.append((x, y))
                                grid[x][y] = "0"

        return num_islands


grid = [
    ["1", "1", "0", "1", "1"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

grid2 = [
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
]
s = Solution()
# print(s.numIslands(grid))
print(s.numIslands(grid2))
print(s.numIslands_2(grid2))

# cProfile.run('s.numIslands_1(grid2)')
# cProfile.run('s.numIslands_2(grid2)')
