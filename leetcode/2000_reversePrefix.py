class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = []
        num = 0
        for i, s in enumerate(word):
            res.append(s)
            if s == ch:
                num = i
                break
        if num > 0:
            res.reverse()
            return "".join(res) + word[num + 1:]
        return word

    def reversePrefix_1(self, word: str, ch: str) -> str:
        """
        超短解法
        @param word:
        @param ch:
        @return:
        """
        i = word.find(ch) + 1
        return word[:i][::-1] + word[i:]


word = "abcdefd"
ch = "d"
s = Solution()
print(s.reversePrefix(word, ch))
print(s.reversePrefix_1(word, ch))
