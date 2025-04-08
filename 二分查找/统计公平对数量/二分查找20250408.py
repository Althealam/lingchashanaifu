# 思路：
# 求解lower<=nums[i]+nums[j]<=upper，也就是求解lower-nums[j]<=nums[i]<=upper-nums[j]（在[0, j]的范围内，找到满足这个条件的数组对）
# 求出nums[i]<=upper-nums[j]的个数，减去nums[i]<lower-nums[j]的个数，就是答案

# bisect_left和bisect_right的区别
# （1）bisect_left用于在有序列表中找到元素x应该插入的最左位置
# （2）bisect_right用于在有序列表中找到元素x应该插入的最右位置

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        for j, num in enumerate(nums):
            # 求解<=upper-nums[j]的nums[i]个数
            # 在[0,j]的范围内，第一个大于等于upper-num的元素的下标
            right=self.bisect_right(nums, upper-num, 0, j)
            # 求解<lower-nums[j]的nums[i]个数
            # 在[0,j]的范围内，第一个大于lower-num的元素的下标
            left=self.bisect_left(nums, lower-num, 0, j)
            ans+=right-left
        return ans
    
    def bisect_left(self, nums, x, left, right):
        while left<right:
            mid=(left+right)//2
            if nums[mid]<x:
                left=mid+1
            else:
                right=mid
        return left
    

    def bisect_right(self, nums, x, left, right):
        while left<right:
            mid=(left+right)//2
            if x<nums[mid]: # [left, mid)
                right=mid
            else:
                left=mid+1
        return left
