from collections import Counter
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        tmp = Counter()
        for data in edges:
            for num in data:
                tmp[num] += 1
                if tmp[num] > 1:
                    return num
        return 0

    def findCenter_1(self, edges: List[List[int]]) -> int:
        """
        更精简的解法
        """
        return edges[0][0] if edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1] else edges[0][1]


s = Solution()
print(s.findCenter([[1, 2], [2, 3], [4, 2]]))
