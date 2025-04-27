# 1. dp数组以及下标的含义：dp[i]表示组成总和为i的元素组合的个数为dp[i]
# 2. 递推公式：
# （1）使用nums[j]：dp[j-nums[j]]
# （2）不使用nums[j]：dp[j]
# 3. 初始化：dp[0]=1 背包是target，物品是nums
# 4. 遍历顺序：本题是求排列数，因此是先背包后物品

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(target+1): # 遍历物品
            for j in range(len(nums)): # 遍历背包
                if i>=nums[j]:
                    dp[i]+=dp[i-nums[j]]
        return dp[-1]