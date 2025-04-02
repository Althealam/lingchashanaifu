class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        ans=0 # 统计得分小于K的子数组数目
        lst_sum=0 # 连续子数组的和
        for right in range(len(nums)):
            lst_sum+=nums[right]
            # 连续子数组的和加上右端点的值
            while lst_sum*(right-left+1)>=k: # 需要保证连续子数组的和严格小于k
                lst_sum-=nums[left]
                left+=1
            ans+=right-left+1 # 得分小于K的子数组数量为right-left+1（由于本题都是正数，因此只要某个子数组满足条件，那么该子数组的子数组也一定满足条件）
            # 对于左端点为left，右端点为right的子数组，其子数组的数量为right-left+1（固定右端点一定是right，但是左端点可以是left到right之间的任意一个）
        return ans