# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # [0,n-2]==>(-1, n-1)
        left=-1
        right=len(nums)-1
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]>nums[mid+1]: # 蓝色
                right=mid
            else:
                left=mid
        return right
