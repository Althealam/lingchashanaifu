
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans=0 # 记录最多k个重复元素的最长子数组的长度
        left=0
        cnt=Counter()
        for right in range(len(nums)):
            cnt[nums[right]]+=1
            while cnt[nums[right]]>k: # 本题和无重复字符的最长子串类似，不同的是限制子串内的字符出现次数不可以超过k
                cnt[nums[left]]-=1
                left+=1
            ans=max(ans, right-left+1)
        return ans