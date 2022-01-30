class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ele_list = []
        res = 0
        for i, e in enumerate(s):
            if e not in ele_list:
                ele_list.append(e)
                res = max(res, len(ele_list))
            else:
                while e in ele_list:
                    ele_list.pop(0)
                ele_list.append(e)

        return res

    def lengthOfLongestSubstring_1(self, s: str) -> int:
        ele_list = set()
        n = len(s)
        rk, res = 0, 0
        for i in range(n):
            if i != 0:
                ele_list.remove(s[i - 1])
            while rk < n and s[rk] not in ele_list:
                ele_list.add(s[rk])
                rk += 1
            res = max(res, rk - i)
        return res


s = Solution()
# 第一种方法的内存消耗略小
print(s.lengthOfLongestSubstring('aab'))
# 第二种方法执行速度更快，因为使用了hashSet
print(s.lengthOfLongestSubstring_1('aab'))
