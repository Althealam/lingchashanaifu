# 分析：本题的最后一个数字（nums[-1]）要么是最小值，要么在最小值的右侧
# 由此我们可以在0到n-2中二分
# （1）nums[mid]>nums[n-1]：nums一定是被分为左右两个递增段的，第一段的所有元素均大于第二段的所有元素，最小值在第二段，所以nums[mid]一定在最小值的左边（这是因为数组本来是递增的，出现nums[mid]>nums[n-1]那么一定是分成了两个递增段）
# （2）nums[mid]<nums[n-1]：有可能nums[mid]在第二段，也有可能此时只有一段，那么nums[mid]要么是最小值，要么在最小值右边

# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=-1
        right=len(nums)-1
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]<nums[-1]: # nums[mid]可能在第二段，也可能此时只有一段
                right=mid
            else: # nums被分成了两段，nums[mid]在最小值的左边
                left=mid
        return nums[right]

        