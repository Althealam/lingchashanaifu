# 1. dp数组以及下标的含义：dp[j]表示装满容量为j的背包的最长子序列长度为dp[j]
# 2. 递推公式
# （1）不使用nums[i-1]：dp[j]
# （2）使用nums[i-1]：dp[j-nums[i-1]]+1
# dp[i][j]=max(dp[j], dp[j-nums[i-1]]+1)
# 3. 初始化：全部初始化为负无穷 
# 4. 遍历顺序：先遍历物品，后遍历背包，背包为逆序

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp=[float('-inf')]*(target+1)
        dp[0]=0
        for i in range(1, len(nums)+1): # 遍历从1到len(nums)的物品
            for j in range(target, -1, -1):
                if j>=nums[i-1]:
                    dp[j]=max(dp[j], dp[j-nums[i-1]]+1)
        return dp[target] if dp[target]!=float('-inf') else -1