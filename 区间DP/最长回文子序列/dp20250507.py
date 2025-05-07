# 1. dp数组以及下标的含义：dp[i][j]表示区间[i+1, j-1]内的最长回文子序列的长度为dp[i][j]
# 2. 递推公式
# （1）s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2
# （2）s[i]!=s[j]：dp[i][j]=max(dp[i+1][j], dp[i][j-1])
# 3. 初始化：dp[0][0]=1 如果i==j就初始化为1
# 4. 遍历顺序：dp[i][j]依赖于dp[i+1][j-1]，因此i应该倒叙遍历（从i+1推导过来），j应该正序遍历（j从0推导过来）
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp=[[0]*len(s) for _ in range(len(s))]
        # 初始化
        for i in range(len(s)):
            for j in range(len(s)):
                if i==j:
                    dp[i][j]=1
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]

        