# 思路：定义i, left, right，计算nums[i]+nums[left]+nums[right]
# 每次遍历的时候都更新差值最小的和
# 时间复杂度：O(n**2)
# 1. 排序：O(nlogn)
# 2. 遍历：O(n**2)
# 空间复杂度：O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best=10**6
        for i in range(len(nums)-2):
            left=i+1 # 左指针
            right=len(nums)-1 # 右指针
            while left<right: 
                sum_=nums[i]+nums[left]+nums[right]
                if sum_==target: # 如果有三数之和等于target，直接返回target
                    return target
                best=self.update(sum_, best, target) # 更新差值最小的和
                if sum_>target:
                    right-=1
                    while left<right and nums[right]==nums[right+1]: # 去重right
                        right-=1
                if sum_<target:
                    left+=1
                    while left<right and nums[left]==nums[left-1]: # 去重left
                        left+=1
        return best
        
    def update(self, cur, best, target): # 更新最好的差值best
        if abs(cur-target)<abs(best-target):
            best=cur
        # 如果cur-target的值小于best-target，说明最好的差值是cur-target，那么最好的值是cur
        return best


