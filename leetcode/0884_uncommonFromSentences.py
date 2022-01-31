from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # 使用python3内置的Counter生成每个单词及对应次数的dict
        res = Counter(s1.split()) + Counter(s2.split())
        result = []
        for k, v in res.items():
            if v == 1:
                result.append(k)

        return result


s1 = "this apple is sweet"
s2 = "this apple is sour"
s = Solution()
print(s.uncommonFromSentences(s1, s2))
