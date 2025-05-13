# 思路：
# 1. 通过求该柱子左边和右边第一个比他矮的柱子，由此来求宽度right-left-1
# （1）如果i左侧的小于h的最近元素的下标left，如果不存在则为-1。当求出了left后，left+1就是矩形最左边那根柱子
# （2）如果i右侧的小于h的最近元素的下标right，如果不存在则为n。当求出了right后，right-1就是矩形最右边的那根柱子
# 2. 通过柱子的基准来确定高度h
# 单调栈中存储的是待排查是否为最小柱子的元素，而不是还没找到答案的元素

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[-1]*n
        right=[n]*n
        st=[]
        for i in range(len(heights)):
            while st and heights[i]<=heights[st[-1]]:  # 当前遍历的元素比栈顶元素要小，说明栈顶元素的右边的第一个更小元素就是当前的柱子
                right[st.pop()]=i
            if st: # 弹出栈顶元素，直到当前遍历的元素比栈顶元素要大，说明当前元素的左边的第一个更小元素就是栈顶元素
                left[i]=st[-1]
            st.append(i)
        
        ans=0
        for h, l, r in zip(heights, left, right):
            ans=max(ans, h*(r-l-1))
        return ans
