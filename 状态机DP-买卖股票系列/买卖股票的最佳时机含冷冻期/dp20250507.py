# 1. dp数组以及下标的含义：
# dp[i][0]表示第i天为持有股票的状态下拥有的最大利润
# dp[i][1]表示第i天为不持有股票的状态拥有的最大利润
# dp[i][2]表示第i天的当天卖出股票的状态拥有的最大利润
# dp[i][3]表示第i天为冷冻期的状态拥有的最大利润
# 2. 递推公式
# （1）dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][3]-prices[i]) 前一天持有股票、前一天不持有股票今天持有股票、前一天冷冻期今天持有股票
# （2）dp[i][1]=max(dp[i-1][1], dp[i-1][3]) 前一天不持有股票 保持冷冻期的状态
# （3）dp[i][2]=dp[i-1][0]+prices[i] 昨天持有股票今天卖出股票
# （4）dp[i][3]=dp[i-1][2] 昨天卖出股票今天是冷冻器
# 3. 初始化：dp[i][0]=-prices[0] 
# 4. 遍历顺序：从前向后遍历
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0]*4 for _ in range(len(prices))]
        for i in range(len(prices)):
            dp[i][0]=-prices[0]
        for i in range(1, len(prices)):
            dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][3]-prices[i])
            dp[i][1]=max(dp[i-1][1], dp[i-1][3])
            dp[i][2]=dp[i-1][0]+prices[i]
            dp[i][3]=dp[i-1][2]
        return max(dp[-1][1], dp[-1][2], dp[-1][3])

        