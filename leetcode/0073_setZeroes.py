from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        x_set = set()
        y_set = set()
        for x, axis in enumerate(matrix):
            for y, num in enumerate(axis):
                if num == 0:
                    x_set.add(x)
                    y_set.add(y)

        for x, axis in enumerate(matrix):
            for y in range(len(axis)):
                if x in x_set or y in y_set:
                    matrix[x][y] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
s = Solution()
s.setZeroes(matrix)
print(matrix)
