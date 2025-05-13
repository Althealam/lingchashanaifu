# 需要什么样的数据结构：
# 1. 双端队列：移除最左边的元素；移除最右边的元素；在最右边插入元素
# 2. 单调性：从队首到队尾单调递减

# 时间复杂度：O(n)，每个元素最多入队出队一次
# 空间复杂度：O(k, min(len(set(nums)))) 双端队列中最多有k个元素
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        q=deque()
        for i, x in enumerate(nums): # x=nums[i]
            # 1. 元素进入窗口
            while q and nums[q[-1]]<=x:
                q.pop()
            q.append(i)

            # 2. 元素离开窗口
            if i-q[0]>=k:
                q.popleft()

            # 3. 记录答案
            if i>=k-1:
                ans.append(nums[q[0]]) # 队首元素是最大值
        return ans

        