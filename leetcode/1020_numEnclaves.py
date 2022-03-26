from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        res = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y,):
            for now_x, now_y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= now_x < m and 0 <= now_y < n and grid[now_x][now_y] == 1:
                    grid[now_x][now_y] = 0
                    dfs(now_x, now_y)

        for i in (0, m - 1):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    dfs(i, j)

        for i in range(m):
            for j in (0, n - 1):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    dfs(i, j)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 1:
                    res += 1
        return res


so = Solution()
grid = [[0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1]]
print(so.numEnclaves(grid))
