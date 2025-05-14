# 思路：求出nums的前缀和s后，通过暴力算法，枚举出所有满足i>j并且s[i]-s[j]>=k的子数组[j,i)，取其中最小的i-j作为答案，这个暴力算法的时间复杂度为O(n**2)
# 可以遍历s，用单调队列来维护遍历过的s[i]，并且及时移除无用的s[i]

# 本题的策略：对于每个位置i，维护之前所有的前缀和prefix[j]，找出prefix[i]-prefix[j]>=k，使得i-j最小
# 因此我们使用单调队列可以高效的维护候选的前缀和索引j

# 注意：本题不能使用双指针，因为数组中有负数
# 滑动窗口/双指针适用的场景是：1. 数组元素全部为负数 2. 希望找到某个满足条件的子数组
# 因为非负数的情况下：如果当前窗口[left, right]的和超过了目标值k，移动左指针可以减少和；如果窗口和小于k，移动右指针可以增加和

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        # 构造前缀和数组
        prefix_sum=[0]*(n+1)
        for i in range(n):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        
        # 初始化答案为最大值
        res=float('inf')
        dq=deque()

        for i in range(n+1):
            # 检查当前的前缀和-队头前缀和>=k，更新最短长度
            while dq and prefix_sum[i]-prefix_sum[dq[0]]>=k:
                res=min(res, i-dq.popleft())
            
            # 保持队列单调递增
            while dq and prefix_sum[i]<=prefix_sum[dq[-1]]:
                dq.pop()
        
            dq.append(i)

        return res if res!=float('inf') else -1