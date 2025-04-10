# 分析：
# 方法一：
# 1. 找最小值i
# 2. 在第一段或者第二段中查找target
# 如果target>nums[n-1]，那么target在第一段[0, i-1]中，在[0, i-1]中二分查找target
# 如果target<=nums[n-1]
# （1）i=0：nums是递增的，直接在[0, n-1]中二分查找target
# （2）i>0：target一定在第二段[i, n-1]中，在[i, n-1]中二分查找target
# 上述两种情况可以合并成在[i, n-1]中二分查找target

class Solution:
    # 153. 寻找旋转排序数组的最小值，返回下标
    def findmin(self, nums):
        left=-1
        right=len(nums)-1
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]<nums[-1]: # 最小值在mid的左侧（代表mid现在在第二段，或者是只有一段，因此最小值在mid的左侧）
                right=mid
            else: # 最小值在mid的右侧（代表mid现在在第一段，并且一定有两段，那么最小值一定在第二段，因此是在mid的右侧）
                left=mid
        return right
    
    # 有序数组中找target的下标
    def lower_bound(self, nums, left, right, target):
        while left+1<right: # 开区间 (left, right)
            mid=(left+right)//2
            if nums[mid]>=target: # (left, mid)
                right=mid
            else: # (mid, right)
                left=mid
        return right if nums[right]==target else -1

    # 寻找target（要求时间复杂度为O(nlogn)）
    def search(self, nums: List[int], target: int) -> int:
        i=self.findmin(nums)
        if target>nums[-1]: # target在第一段
            return self.lower_bound(nums, -1, i, target)
        return self.lower_bound(nums, i-1, len(nums), target) # target在第二段

        
        