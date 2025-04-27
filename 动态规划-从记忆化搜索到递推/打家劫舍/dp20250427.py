# 1. dp数组以及下标的含义：dp[i]表示偷[0,i]的房屋时能够偷窃到的最高金额为dp[i]
# 2. 递推公式：
# （1）偷i：dp[i-2]+nums[i]
# （2）不偷i：dp[i-1]
# dp[i]=max(dp[i-2]+nums[i], dp[i-1])
# 3. 初始化：dp[0]=nums[0]
# 4. 遍历顺序：从前向后遍历

class Solution: 
    def rob(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1, len(nums)):
            dp[i]=max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]