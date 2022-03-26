from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        point_list = []
        i = 0
        for op in ops:
            if op == '+':
                point_list.append(point_list[i - 1] + point_list[i - 2])
            elif op == 'D':
                point_list.append(point_list[i - 1] * 2)
            elif op == 'C':
                point_list.pop()
            else:
                point_list.append(int(op))

        return sum(point_list)


s = Solution()
print(s.calPoints(["5", "2", "C", "D", "+"]))
