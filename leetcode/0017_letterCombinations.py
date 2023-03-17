from collections import deque
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        template = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        tmp = []

        def backtrace(index: int):
            if index == len(digits):
                res.append("".join(tmp))
                return
            for character in template[digits[index]]:
                tmp.append(character)
                backtrace(index + 1)
                tmp.pop()

        backtrace(0)
        return res

    def letterCombinations2(self, digits: str) -> List[str]:
        """
        使用bfs完成回溯
        """
        if not digits:
            return []

        template = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        q = deque()
        for character in template[digits[0]]:
            q.append(character)
        index = 1

        while index < len(digits):
            for _ in range(len(q)):
                cur = q.popleft()
                for character in template[digits[index]]:
                    q.append(cur + character)
            index += 1
        return list(q)

s = Solution()
print(s.letterCombinations("2345"))
print(s.letterCombinations2("975"))
