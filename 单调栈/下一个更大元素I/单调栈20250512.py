# 思路：栈中存储还没算出下一个更大元素的那些数
# 只要遍历到比栈顶元素更大的数，就代表栈顶元素找到了答案，记录答案后弹出栈顶元素即可

# 时间复杂度：O(n+m) 其中n是nums1的数组长度，m是nums2的数组长度
# 空间复杂度：O(n)，存储nums1的映射
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        st=[]
        idx={x: i for i, x in enumerate(nums1)}
        for num2 in nums2:
            while st and num2>st[-1]:
                num1=st.pop() # 弹出栈顶元素，该元素找到了答案
                ans[idx[num1]]=num2
            if num2 in idx:
                st.append(num2)
        return ans
            


