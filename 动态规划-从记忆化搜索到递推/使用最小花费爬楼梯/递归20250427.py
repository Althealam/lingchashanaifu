# 1. dp数组以及下标的含义：dp[i]表示爬到第i个台阶的最低花费为dp[i]
# 2. 递推公式：
# （1）爬一个台阶：dp[i-1]+cost[i-1]
# （2）爬两个台阶：dp[i-2]+cost[i-2]
# dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
# 3. 初始化：dp[0]=0 dp[1]=0
# 4. 遍历顺序：从前向后遍历

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        for i in range(2, len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]
        