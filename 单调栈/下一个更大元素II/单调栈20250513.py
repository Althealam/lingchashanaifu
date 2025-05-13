# 思路：栈中记录还没算出下一个更大元素的那些数的下标
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums) # 存储每个元素的下一个最大元素（循环数组）
        st=[] # 单调栈
        for i in range(len(nums)*2): # 遍历两个数组
            while st and nums[i%len(nums)]>nums[st[-1]]: # 当前遍历到的元素i是栈顶元素的答案
                ans[st.pop()]=nums[i%len(nums)] # 更新答案值
            if i<len(nums):
                st.append(i)
        return ans
        