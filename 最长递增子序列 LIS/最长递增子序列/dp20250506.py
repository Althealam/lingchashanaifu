# 1. dp数组以及下标的含义：dp[i]表示以nums[i]为结尾的最长严格递增子序列的长度
# 2. 递推公式
# 位置i的最长子序列长度为0到i-1的最长严格递增子序列的长度加1（需要确保nums[i]大于nums[j]）
# dp[i]=max(dp[j]+1, dp[i])
# 3. 初始化：全部初始化为1
# 4. 遍历顺序：先遍历i，再遍历j

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        if len(nums)==1:
            return 1
        result=0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[j]+1, dp[i])
            result=max(result, dp[i])
        return result

        