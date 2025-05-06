# 1. dp数组以及下标的含义：dp[i][j]表示以text1[i-1]为结尾和以text2[j-1]为结尾的最长公共子序列长度
# 2. 递推公式
# （1）text1[i-1]==text2[j-1]：dp[i][j]=dp[i-1][j-1]+1
# （2）text1[i-1]!=text2[j-1]：dp[i][j]=max(dp[i-1][j], dp[i][j-1])
# 3. 初始化：全部初始化为0 dp[i][0]=0 dp[0][j]=0
# 4. 遍历顺序：先text1再text2

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        result=0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                result=max(result, dp[i][j])
        return result