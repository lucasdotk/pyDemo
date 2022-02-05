from collections import deque
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        回溯算法，核心在于将走过的点先置0，在完成搜索后再置回原值
        @param grid:
        @return:
        """
        ans = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(x: int, y: int, gold: int):
            gold += grid[x][y]
            nonlocal ans
            ans = max(gold, ans)

            tmp = grid[x][y]
            grid[x][y] = 0

            for now_x, now_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= now_x < m and 0 <= now_y < n and grid[now_x][now_y] > 0:
                    dfs(now_x, now_y, gold)

            grid[x][y] = tmp

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dfs(i, j, 0)

        return ans

    def getMaximumGold_1(self, grid: List[List[int]]) -> int:
        """
        bfs算法，每次走过一个点后，将这个点pop，然后把接下来可能走的所有点加入队列
        @param grid:
        @return:
        """
        m, n = len(grid), len(grid[0])
        Q = deque([])
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    Q.append([i, j, grid[i][j], [(i, j)]])
                    ret = max(ret, grid[i][j])
        while Q:
            i, j, total, visited = Q.popleft()
            ret = max(ret, total)
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] != 0 and (x, y) not in visited:
                    Q.append([x, y, total + grid[x][y], visited + [(x, y)]])
        return ret


s = Solution()
print(s.getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
print(s.getMaximumGold_1([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
