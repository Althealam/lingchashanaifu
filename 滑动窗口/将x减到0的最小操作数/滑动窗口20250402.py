# 分析：本题的目标是找到一个最长的连续子数组，其和为sum(nums)-x（因为当其为最长的时候，其操作数就是最小的：操作数+连续子数组长度=len(nums)）
# 由于只能移除睡着最左边或者最右边的元素，因此left和right都是需要进行滑动的（不像之前将right去遍历len(nums)）
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        # 如果target<0，说明sum(nums)<x，那么不管用nums中的哪个元素来做减法，都没办法把x变成0
        if target<0:
            return -1
        left=0 # 滑动窗口左端点
        right=0 # 滑动窗口右端点
        ans=-1 # 和为target的连续子数组的长度
        total=0 # 滑动窗口中的数字总和
        while right<len(nums):
            total+=nums[right]
            while total>target:
                total-=nums[left]
                left+=1
            if total==target:
                ans=max(ans, right-left+1)
            right+=1
        return -1 if ans==-1 else len(nums)-ans # 操作数就是nums的长度减去最长连续子数组的长度