# 需要记录的元素
# 1. 栈顶元素 2. 栈顶下面的数 3. 下标差（底部）

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        st=[]
        for i, h in enumerate(height):
            while st and h>=height[st[-1]]:
                bottom_h=height[st.pop()]
                if len(st)==0:
                    break
                left=st[-1]
                dh=min(height[left], h)-bottom_h
                ans+=dh*(i-left-1)
            st.append(i)
        return ans        