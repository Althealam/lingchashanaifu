# 分析：本题和“无重复字符的最长子串”相同思路
# 计算滑动窗口内的乘积：（1）乘积大于k：s除以left的值 更新left（2）乘积小于k：更新ans
# 注意：本题求的是乘积小于k的子数组的数量，而“无重复字符的最长子串”求的是超过target的最小的子数组的长度
# 因此本题的滑动窗口策略不同

# 时间复杂度：O(n) 
# 分析思路和上题一样，都是看left+=1的次数
# 空间复杂度：O(1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        ans=0 # 计算乘积小于k的子数组的数量
        s=1 # 计算滑动窗口内的元素乘积
        left=0
        for right in range(len(nums)):
            s*=nums[right]
            while s>=k: # 如果乘积大于等于k，则左移left，缩小滑动窗口的长度
                s/=nums[left]
                left+=1
            ans+=right-left+1 # 子数组的数目（注意，右端点是固定的，因此对于每个右端点，其滑动窗口乘积和小于k的数量都是right-left+1）
            # 因为：如果[l, r]的乘积小于k，那么[l+1, r], ..., [r, r]的子数组的乘积也是小于k的
        return ans

        