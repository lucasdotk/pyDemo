class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        dp = {}
        fib = [1, 1]
        prev, cur = 1, 1
        while cur < k:
            cur, prev = cur + prev, cur
            fib.append(cur)

        dp[0] = 0
        for i in range(1, k + 1):
            for ele in fib:
                if ele > i:
                    break
                dp[i] = dp[i - ele] + 1

        return dp[k]

    def findMinFibonacciNumbers_1(self, k: int) -> int:
        """
        经过证明，必须选取比k小的最大斐波那契值，所以使用贪心算法解决此题
        推论主要有两点：1两个斐波那契数不可能相邻，因为相邻的数可以由下一个数代替；2如果一个斐波那契数出现两次，则可以由f(x-2)和f(x+1)代替
        即不存在相邻的斐波那契数和重复的斐波那契数；可以通过公式推算出，必须选择小于k的那个最大的斐波那契数
        @param k:
        @return:
        """
        fib = [1, 1]
        prev, cur = 1, 1
        while cur < k:
            cur, prev = cur + prev, cur
            fib.append(cur)
        i = len(fib) - 1
        ans = 0
        while k:
            if k >= fib[i]:
                k -= fib[i]
                ans += 1
            i -= 1
        return ans


s = Solution()
print(s.findMinFibonacciNumbers(90))
print(s.findMinFibonacciNumbers_1(100))
