# 本题是长度固定为k的滑动窗口最大值问题 我们需要求解的是f[0], f[1], ... , f[i-1]的出最大值
# 我们需要维护一个f值从左到右严格递减的单调队列（双端队列）
# 在计算f[i]的时候，需要保证队首就是转移来源最大值的下标
# 1. 出：如果队首小于i-k，则弹出队首
# 2. 转移：f[i]=f[q[0]]+nums[i]。其中q[0]表示单调队列q的队首，此时队首就是转移来源最大值的下标
# 3. 入：不断弹出队尾，直到队列为空，或者f[i]小于队尾对应的f值为止，然后将i加到队尾

# 时间复杂度：O(n)，每个下标最多出队入队一次，因此循环次数最多为n
# 空间复杂度：O(n)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        f=[0]*n
        f[0]=nums[0]
        q=deque([0])
        for i in range(1, n):
            # 1. 出
            if q[0]<i-k:
                q.popleft()
            # 2. 转移
            f[i]=f[q[0]]+nums[i]
            # 3. 入
            while q and f[i]>=f[q[-1]]:
                q.pop()
            q.append(i)
        return f[-1]
