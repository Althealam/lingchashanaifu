# 1. dp数组以及下标的含义：
# dp[i][0]表示第i天第一次持有股票的状态所有的最大利润
# dp[i][1]表示第i天第一次不持有股票的状态所有的最大利润
# dp[i][2]表示第i天第二次持有股票的状态所有的最大利润
# dp[i][3]表示第i天第二次不持有股票的状态所有的最大利润
# dp[i][k](k为奇数)表示第i天不持有股票的状态所有的最大利润；dp[i][k]（k为偶数）表示第i天持有股票的状态所有的最大利润
# 2. 递推公式
# （1）dp[i][0]=max(dp[i-1][0], -prices[0])
# （2）dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i]）
# （3）dp[i][2]=max(dp[i-1][2], dp[i-1][1]-prices[i])
# （4）dp[i][3]=max(dp[i-1][3], dp[i-1][2]+prices[i])
# dp[i][k]=max(dp[i-1][k], dp[i-1][k-1]-prices[i])（k为偶数）
# dp[i][k]=max(dp[i-1][k], dp[i-1][k-1]+prices[i])（k为奇数）
# 3. 初始化：dp[0][0]=-prices[0] dp[i][0]=-prices[i] j为偶数
# 4. 遍历顺序：从前向后遍历
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp=[[0]*2*k for _ in range(len(prices))]
        for j in range(2*k):
            if j%2==0:
                dp[0][j]=-prices[0]
        for i in range(1, len(prices)):
            for j in range(2*k):
                if j==0:
                    dp[i][j]=max(dp[i-1][0], -prices[i])
                elif j%2==0:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+prices[i])
        return dp[-1][-1]