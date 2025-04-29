# 1. dp数组以及下标的含义：表示凑出金额为j的方法为dp[j]
# 2. 递推公式
# （1）使用coin：dp[j-coin]
# （2）不使用coin：dp[j]
# dp[j]+=dp[j-coin]
# 3. 初始化：全部初始化为0 dp[0]=1
# 4. 遍历顺序：先遍历物品，后遍历背包（本题为组合数，因此背包不需逆序，注意，当求解组合数并且为一维数组的时候，遍历背包不需要逆序）

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for j in range(amount+1):
                if j>=coin:
                    dp[j]+=dp[j-coin]
        return dp[-1]
