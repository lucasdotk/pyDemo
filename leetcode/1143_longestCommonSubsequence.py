class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = []
        len1 = len(text1)
        len2 = len(text2)

        if len1 > len2:
            text1, text2 = text2, text1

        for i, s1 in enumerate(text1):
            for s2 in text2:
                if dp[i] == i + 1:
                    break
                if s1 == s2:
                    pass

aa = "ts_code,trade_date,close,turnover_rate,turnover_rate_f,volume_ratio,pe,pe_ttm,pb,ps,ps_ttm,dv_ratio,dv_ttm,total_share,float_share,free_share,total_mv,circ_mv".split(",")

for a in aa:
    print(a + " double,")