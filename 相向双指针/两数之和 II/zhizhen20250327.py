# 分析：数组已经有序了，因此可以按照双指针的思路解决这道题
# 思路：双指针每次指向头部和尾部的两个元素。如果nums[left]+nums[right]>target，那么right-=1；如果nums[left]+nums[right]<target，那么left+=1；如果nums[left]+nums[right]==target，那么找到了left和right
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                break
        return [left+1, right+1]
            
        