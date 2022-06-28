from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        append_new = False
        length = len(intervals)
        for i, two_num in enumerate(intervals):

            # 如果待插入元素在当前元素左侧
            if two_num[0] > newInterval[1]:
                # 并且未被插入到列表中
                if not append_new:
                    res.append(newInterval)
                    append_new = True
                res.append(two_num)
                continue

            # 如果待插入元素在当前元素右侧
            if two_num[1] < newInterval[0]:
                res.append(two_num)
                continue

            newInterval = [min(two_num[0], newInterval[0]), max(two_num[1], newInterval[1])]
            if i + 1 < length and intervals[i + 1][0] > newInterval[1]:
                res.append(newInterval)
                append_new = True

        if not append_new:
            res.append(newInterval)

        return res


s = Solution()
print(s.insert([[1, 3], [6, 9]], [2, 5]))
print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(s.insert([[1, 5]], [2, 3]))
print(s.insert([], [2, 3]))
print(s.insert([[1, 5]], newInterval=[2, 7]))
print(s.insert([[1, 5]], [0, 0]))
