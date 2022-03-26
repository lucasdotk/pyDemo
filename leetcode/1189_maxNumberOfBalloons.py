import sys
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_dict = Counter(text)
        target_dict = Counter("balloon")
        res = sys.maxsize
        for k,v in target_dict.items():
            if not text_dict[k]:
                return 0
            res = min(res, text_dict[k] // v)
        return res


so = Solution()
print(so.maxNumberOfBalloons("loonbalxballpoon"))
