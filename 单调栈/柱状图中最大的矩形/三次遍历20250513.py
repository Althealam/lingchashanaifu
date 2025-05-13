# 思路：
# 1. 通过求该柱子左边和右边第一个比他矮的柱子，由此来求宽度right-left-1
# （1）如果i左侧的小于h的最近元素的下标left，如果不存在则为-1。当求出了left后，left+1就是矩形最左边那根柱子
# （2）如果i右侧的小于h的最近元素的下标right，如果不存在则为n。当求出了right后，right-1就是矩形最右边的那根柱子
# 2. 通过柱子的基准来确定高度h
# 单调栈中存储的是待排查是否为最小柱子的元素，而不是还没找到答案的元素

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)

        # 求出每个元素左边的第一个比他小的元素
        left=[-1]*n
        st=[] # 栈中存储还没找到答案的元素
        for i in range(len(heights)):
            while st and heights[i]<=heights[st[-1]]:
                st.pop() # 当前柱子比栈顶还小，说明栈顶不是左边第一个小的，要继续弹出
            if st: # 找到了当前柱子比栈顶大的元素，那么当前柱子的左边的第一个小的位置就是栈顶元素
                left[i]=st[-1] # 栈顶是左边第一个比当前柱子小的位置
            st.append(i)
        
        # 求出每个元素右边第一个比他小的元素
        right=[n]*n
        st=[]
        for i in range(n-1, -1, -1):
            while st and heights[i]<=heights[st[-1]]:
                st.pop() # 当前柱子比栈顶元素小，说明栈顶元素不可能是右边第一个更小柱子，因此要继续弹出栈顶元素
            if st: # 找到了比栈顶元素大的柱子，那么栈顶元素就是当前柱子的右边的第一个更小柱子
                right[i]=st[-1] # 栈顶就是右边第一个比当前小的柱子的位置
            st.append(i) 
        
        ans=0 # 矩形的最大面积
        for h, l, r in zip(heights, left, right):
            ans=max(ans, h*(r-l-1)) # 宽度为r-l-1，高度为h
        return ans
            