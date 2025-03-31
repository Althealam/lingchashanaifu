# 分析：假设已经排序1<=a<=b<=c
# 有效三角形的要求：a+b>c, a+c>b, b+c>a
# 显然a+c>b成立（a+c>a+b>b），显然b+c>a成立（b+c>b+a>a），因此我们只需要证明a+b>c即可
# 本题中，令nums[i]为c，nums[left]为a，nums[right]为b
# 当nums[left]+nums[right]-nums[i]>0的时候，会出现[left, right]的区间内的任意的left都满足条件
# 因为：nums[k]+nums[right]-nums[i]>nums[left]+nums[right]-nums[i]（k>left, nums[k]>nums[left]），因此可以随意移动left

# 时间复杂度：O(n**2)
# 1. 排序：O(nlogn)
# 2. 双指针遍历：O(n**2)
# 空间复杂度：O(logn)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0  # 计算可以组成三角形的数量
        nums.sort()
        for i in range(2, len(nums)): # 让i为c
            left=0 # 让left为a
            right=i-1 # 让right为b
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    count+=right-left # 计算有效三角形的个数
                    right-=1
                else:
                    left+=1
        return count
