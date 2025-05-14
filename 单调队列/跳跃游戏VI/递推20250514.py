# 递归法
# 1. 定义：f(i)表示从0跳到i，经过的所有数字之和的最大值
# 2. 递推公式：f[i]=max(f[j]+nums[i])，其中j的初始值为max(i-k,0)，最终值为i-1
# 3. 初始值：f[0]=nums[0]
# 4. 答案：f[n-1]

# 时间复杂度：O(nk)
# 空间复杂度：O(n)，递归需要O(n)的栈空间
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        f=[0]*n
        f[0]=nums[0]
        for i in range(1, n):
            f[i]=max(f[max(i-k ,0):i])+nums[i]
        return f[-1]