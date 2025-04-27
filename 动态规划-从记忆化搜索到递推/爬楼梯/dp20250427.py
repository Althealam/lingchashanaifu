# 1. dp数组以及下标的含义：dp表示爬到第i个台阶的时候有dp[i]
# 2. 递推公式
# （1）爬2个台阶：dp[i-2]
# （2）爬1个台阶：dp[i-1]
# dp[i]=dp[i-1]+dp[i-2]
# 3. 初始化：dp[0]=1 dp[1]=1
# 4. 遍历顺序：从前向后遍历

class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2, n+1):
            dp[i]=dp[i-2]+dp[i-1]
        return dp[-1]
        