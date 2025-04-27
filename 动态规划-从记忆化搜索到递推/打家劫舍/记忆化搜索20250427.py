# DP三步：1. 思考回溯怎么写（入参和返回值、递归到哪里、递归边界和入口） 2. 改成记忆化搜索 3. 1:1翻译成di tui

# 1. 当前操作：枚举第i个房子选/不选
# 2. 子问题：从前i个房子中得到的最大金额和
# 3. 下一个子问题，分类讨论：
# （1）不选：从前i-1个房子中得到的最大金额和
# （2）选：从前i-2个房子中得到的最大金额和 
# dfs=max(dfs(i-1), dfs(i-2)+nums[i])

# 1. dp数组以及下标的含义：dp[i]表示偷0到i-1个房屋的时候，能够偷到的最大金额是dp[i]
# 2. 递推公式：
# （1）偷i：dp[i-2]+nums[i]
# （2）不偷i：dp[i-1]

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution: 
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[-1]*n # 缓存之前计算的结果
        def dfs(i):
            if i<0:
                return 0
            if cache[i]!=-1:
                return cache[i]
            res=max(dfs(i-1), dfs(i-2)+nums[i])
            cache[i]=res
            return res
        return dfs(n-1)
