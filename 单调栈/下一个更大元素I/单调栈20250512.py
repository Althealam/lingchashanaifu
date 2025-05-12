# 思路：栈中存储还没算出下一个更大元素的那些数
# 只要遍历到比栈顶元素更大的数，就代表栈顶元素找到了答案，记录答案后弹出栈顶元素即可
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        st=[] # 栈中存储的是nums2中的元素
        idx={x:i for i, x in enumerate(nums1)} # key是元素的值，value是元素的下标 构建元素到下标的映射
        for num in nums2:
            while st and num>st[-1]:
                j=st.pop()
                # 找到了栈顶元素的答案
                ans[idx[j]]=num # 记录答案
            if num in idx: # x在nums1中
                st.append(num) # 把nums1中的元素入栈
        return ans