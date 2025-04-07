# 分析：有序数组上的二分查找大概分为四种类型：>=, <=, <, >（这四种类型可以互相转换，必须>可以转换为>=x+1；<可以转换为<=x-1）
# 并且二分查找有四种方法：闭区间、左闭右开、开区间
# （1）left<=right：闭区间
# （2）left<right：半闭半开区间
# （3）left+1<right：开区间

# 时间复杂度：取决于lower_bound，并且每次都取半，因此是O(logn)
# 空间复杂度：O(1)
class Solution:
    # lower_bound1, lower_bound2, lower_bound3相当于查找target值所在的区间
    def lower_bound1(self, nums, target):
        """
        闭区间写法 [left, right]
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                # [mid+1, right] 闭区间
                left=mid+1
            else:
                # [left, mid-1] 闭区间
                right=mid-1
        # 循环结束后left=right+1，此时nums[left-1]<target而nums[left]=nums[right+1]>=target
        # 因此left就是第一个>=target的元素下标
        return left
    
    def lower_bound2(self, nums, target):
        """
        左闭右开区间写法 [left, right)
        """
        left=0
        right=len(nums) # 左闭右开区间 [left, right)
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1 # [mid+1, right)
            else:
                right=mid # [left, mid)
        return left

    def lower_bound3(self, nums, target):
        """
        开区间写法 (left, right)
        """
        left=-1
        right=len(nums) # (left, right)
        while left+1<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid # (mid, right)
            else:
                right=mid # (left, mid)
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        本题寻找等于target的开始位置和结束位置
        1. 开始位置：找到>=target的位置
        2. 结束位置：找到<=target的位置
        """
        start=self.lower_bound1(nums, target) # 找到第一个等于target的数组的下标
        if start==len(nums) or nums[start]!=target:
            return [-1, -1]
        # 想找到<=target的最后一个数，可以找到>target的第一个数（>target等价于>=target+1）
        # 由于数组已经有序了，因此再将得到的下标减去1即可
        end=self.lower_bound1(nums, target+1)-1
        return [start, end]

        