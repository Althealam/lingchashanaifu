# 1. dp数组以及下标的含义：和为j的时候完全平方数的最少数量为dp[j]
# 2. 递推公式
# （1）使用i：dp[j-i**2]+1
# （2）不使用i：dp[j]
# dp[j]=min(dp[j-i**2]+1, dp[j])
# 3. 初始化：全部初始化为float('inf') dp[0]=0 表示和为0的时候完全平方数的最少数量为0
# 4. 遍历顺序：本题也是求组合数，因此是先物品后背包，并且背包不逆序

class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1, n+1):  # 遍历物品（可以使用自己，因此需要修改为n+1；不可以使用0，因此从1开始遍历）
            for j in range(i*i, n+1): # 遍历背包
                    dp[j]=min(dp[j], dp[j-i*i]+1)
        return dp[-1]
