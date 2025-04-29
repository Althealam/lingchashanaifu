# 1. dp数组以及下标的含义：dp[j]表示装满这个容量为j的背包，这个背包的最大价值为dp[j]
# 2. 递推公式：
# x1+x2=sum(nums) x1=x2==>x1=sum(nums)//2
# （1）不装物品i：dp[j]
# （2）装入物品i：dp[j-nums[i]]+nums[i]
# dp[j]=max(dp[j], dp[j-nums[i]]+nums[i])
# 3. 初始化：dp=[0]*(target_sum+1)
# 4. 遍历顺序：先遍历物品，后遍历背包，背包为逆序

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target_sum=sum(nums)//2
        dp=[0]*(target_sum+1)
        for num in nums:
            for j in range(target_sum, -1, -1):
                if j>=num:
                    dp[j]=max(dp[j], dp[j-num]+num)
        if dp[target_sum]==target_sum:
            return True
        return False
