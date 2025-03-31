# 思路：不停的移动right，让left作为滑动窗口的指针来移动（固定right，移动left，扩展左边界）
# （1）如果s>=target：让left+=1，直到满足s<target为止；同时更新ans的值
# （2）如果s<target：继续移动right指针
# 时间复杂度：
# 循环的次数是left+=1的次数，left最多到n，因此是O(n)
# 空间复杂度：O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        ans=float('inf') # 初始化长度最小的子数组
        s=0 # 计算子数组的和
        left=0 # 左指针
        for right in range(len(nums)): # x:nums[right] 不停的移动右指针
            s+=nums[right]  # 不停的加上右指针的值

            # 单调性
            while s>=target:
                ans=min(ans, right-left+1)
                s-=nums[left]
                left+=1
        return ans if ans<=n else 0

        