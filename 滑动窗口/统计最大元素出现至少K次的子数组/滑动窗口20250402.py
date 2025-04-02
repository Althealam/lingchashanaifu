class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans=0 # 统计最大元素最少出现K次的子数组的个数
        left=0
        count=0 # 统计最大元素出现的次数
        max_num=max(nums) # nums中的最大元素
        for right in range(len(nums)):
            # 如果right的nums值和max_num相同，则增加最大元素出现的次数
            if nums[right]==max_num:
                count+=1
            while count==k:
                if nums[left]==max_num:
                    count-=1
                # 移动left的前提是left的值和max_num不相同。
                # 移动left后，滑动窗口的范围是[left+1, right]
                # 对于右端点为right并且左端点小于left的子数组，max_num的出现次数都至少为k次，因此将答案增加left即可（下标）
                left+=1
            ans+=left
        return ans


        