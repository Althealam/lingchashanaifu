# 时间复杂度：O(n^2)
# （1）排序：O(nlogn)
# （2）遍历数组：O(n^2)
# 空间复杂度：O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # 三元组的顺序并不重要
        # i<j<k
        # 答案中不可以出现重复的三元组
        ans=[]
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]: # 不可以有重复的三元组
                continue
            if nums[i]+nums[i+1]+nums[i+2]>0: # 剪枝
                break
            if nums[i]+nums[-2]+nums[-1]<0: # 剪枝
                break
            left=i+1
            right=n-1
            while left<right:
                sum_=nums[i]+nums[left]+nums[right]
                if sum_>0:
                    right-=1
                elif sum_<0:
                    left+=1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while left<right and nums[r]==nums[left-1]:
                        left+=1
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
        return ans