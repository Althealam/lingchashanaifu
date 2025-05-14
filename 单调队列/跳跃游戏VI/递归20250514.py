# 递归法
# 1. 定义：dfs(i)表示从0跳到i，经过的所有数字之和的最大值
# 2. 递推公式：如果从j调过来，那么有dfs(i)=dfs(j)+nums[i]，其中max(i-k,0)<=j<=i-1
# 枚举j，取转移来源的最大值，那么dfs(i)=max dfs(j)+nums[i]（其中j=max(i-k,0)并且最大到i-1）
# 3. 递归边界：dfs(0)=nums[0]
# 4. 递归入口：dfs(n-1)

# 时间复杂度：O(k**n)，其中n是nums的长度，搜索树可以近似为一颗k叉树，树高为O(n)，因此节点数为k**n
# 空间复杂度：O(n)，递归需要O(n)的栈空间
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        def dfs(i):
            if i==0:
                return nums[0]
            return max(dfs(j) for j in range(max(i-k, 0), i))+nums[i]
        return dfs(len(nums)-1)
        