# 分析：定义双指针left和right
# 只要left<right并且nums[left]+nums[right]>=target，就让right-=1，直到满足nums[left]+nums[right]<target为止，此时有j-i个合法的下标对，将其添加到结果中
# 时间复杂度：O(nlogn)
# （1）排序：O(nlogn)
# （2）双指针遍历：O(n)
# 空间复杂度：O(1)

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count=0 # 统计和小于目标和的下标对数量
        left=0
        right=len(nums)-1
        while left<right:
            # 一直移动right指针，直到满足nums[left]+nums[right]<target为止，此时就找到了对于left而言合法的下标值
            while left<right and nums[left]+nums[right]>=target:
                right-=1
            count+=right-left # 加上合法的下标对
            left+=1 # 移动left指针，开始查找对于left+1而言合法的下标值（不需要复原right，因为上一个left+right<target，那么left+1的合法指针数量只会更少）
            
        return count