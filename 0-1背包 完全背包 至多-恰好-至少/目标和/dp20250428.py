# 1. dp数组以及下标的含义：满足加法的总和值为i的方法数为dp[i]
# 2. 递推公式：dp[j]+=dp[j-nums[i]]
# x1+x2=sum(nums) x1-x2=target x1=(sum(nums)+target)//2 找到x1的方法数即可
# 3. 初始化：dp=[0]*(target_sum+1)（target_sum是目标和，也就是left的背包容量）
# 3. 遍历顺序：先遍历物品，后遍历背包，背包需要逆序，因为本题是一维数组，一般一维数组都需要背包逆序

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums)+target)%2!=0:
            return 0
        if len(nums)==0:
            return 0
        target_sum=(sum(nums)+target)//2
        if target_sum<0:
            return 0
        dp=[0]*(target_sum+1)
        dp[0]=1
        for i in range(len(nums)):
             for j in range(target_sum, -1, -1):
                if j>=nums[i]:
                    dp[j]+=dp[j-nums[i]]
        return dp[-1]
