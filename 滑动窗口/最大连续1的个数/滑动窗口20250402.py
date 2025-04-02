# 缩小窗口的条件：当由1变成0的数量cnt0超过了k
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans=0
        left=0
        cnt0=0 # 统计将1变成0的个数
        for right in range(len(nums)):
            cnt0+=1-nums[right]
            while cnt0>k:
                cnt0-=1-nums[left]
                left+=1
            ans=max(ans, right-left+1)
        return ans 
            

        