class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        tmp = [[] for _ in range(numRows)]
        max_times = numRows - 1
        increase = True
        times = 0
        for e in s:
            tmp[times].append(e)

            if increase:
                times += 1
            else:
                times -= 1

            if times == max_times:
                increase = False
            if times == 0:
                increase = True

        res = ''
        for arr in tmp:
            res += "".join(arr)

        return res


so = Solution()
s = "AB"
numRows = 1
print(so.convert(s, numRows))
