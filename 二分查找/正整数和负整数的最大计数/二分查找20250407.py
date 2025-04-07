# 思路：找到第一个>0的元素的下标i（注意，不包含元素0），那么[0, i-1]的数组都是负整数，[i, len(nums)-1]的数组都是正整数

class Solution:
    def bisect_left(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target: # [mid+1, right]
                left=mid+1
            else: # [left, mid-1]
                right=mid-1
        return left # 第一个大于等于0的数组的下标

    def maximumCount(self, nums: List[int]) -> int:
        neg=self.bisect_left(nums, 0) # 第一个大于等于0的数组的下标
        # 负整数的区间是[0, neg-1] 正整数的区间是[neg, len(nums)-1]
        # 负整数的区间的长度是neg，正整数的区间的长度是len(nums)-neg
        pos=self.bisect_left(nums, 1) # 第一个大于等于1的数组下标
        return max(neg, len(nums)-pos)


        