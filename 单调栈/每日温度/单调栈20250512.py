# 分析
# 1. 先进先出
# （1）记录的数据加在最上面 （2）丢掉数据也先从最上面开始
# 2. 单调性：记录t[i]之前会把所有<=t[i]的数据丢掉，不可能出现上面大下面小

# 时间复杂度：O(n) 每个元素最多会入栈和出栈一次
# 空间复杂度：O(n)，最坏情况下栈内有n个元素 但是由于栈中的元素为30到100个，因此栈最多有71个元素，因此为O(1)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        st=[] # 单调栈
        for i in range(n-1, -1, -1):
            t=temperatures[i]
            while st and t>=temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i]=st[-1]-i
            st.append(i)
        return ans
        