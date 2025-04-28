# 1. dp数组以及下标的含义：dp[j]表示凑到金额为j的最少的硬币个数为dp[j]
# 2. 递推公式：
# （1）要coin：dp[j-coin]+1
# （2）不要coin：dp[j]
# 3. 初始化：全部初始化为float('inf') dp[0]=0
# 4. 遍历顺序：先物品，后背包，由于本题是求组合数，因此遍历背包时不需要逆序
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for j in range(amount+1):
                if j>=coin:
                    dp[j]=min(dp[j-coin]+1, dp[j])
        return dp[amount] if dp[amount]!=float('inf') else -1

