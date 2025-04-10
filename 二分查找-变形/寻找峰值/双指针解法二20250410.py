# 分析：规定nums[-1]==nums[n]=float('-inf')是为了保证数组一定有峰值（如果nums为递减的，那么nums[0]就是峰值；如果nums为递增的，那么nums[n]就是峰值）；同时本题还规定了对于有效的i，都有nums[i]!=nums[i+1]，也就是相邻的数字都是不等的
# 思路：通过比较nums[i]和nums[i+1]的大小关系，从而不断的缩小峰值所在位置的范围（只要不断爬坡，就能找到峰值）
# 这个方法只能找到一个峰值，不能找到多个峰值
# 注意：二分的范围可以是闭区间[0, n-2]，或者开区间(-1, n-1)，也就是说峰值一定不可能是n-1
# 因为有且仅有一个峰值是n-1的话，那么会有nums[0]<nums[1]<nums[2]<...<nums[n-1]>nums[n]=float('-inf')

# 时间复杂度：O(nlogn)（二分法每次都会缩短数组的一半）
# 空间复杂度：O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # [0,n-2]==>(-1, n-1)
        left=-1
        right=len(nums)-1
        # 在常规的二分模版中，直接使用right=len(nums)，right遍历过程中是取不到len(nums)这个值的
        # 这里减去1，主要是为了避免nums[mid+1]越界，而且又不妨碍最终的答案落在len(nums)-1上
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>nums[mid+1]: # 峰顶在右侧
                right=mid
            else: # nums[mid]>nums[mid+1] 峰顶在左侧
                left=mid+1
        return left

