# 缩小窗口的条件：当由1变成0的数量cnt0超过了k
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans=0
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                k-=1
            while k<0:
                if nums[left]==0:
                    k+=1
                left+=1
            ans=max(ans, right-left+1)
        return ans