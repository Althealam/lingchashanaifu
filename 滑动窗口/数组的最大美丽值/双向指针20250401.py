# 分析：由于选的是子序列，因此和元素顺序没有关系，可以对数组进行排序，并且排序后的闭区间也是连续的
# 将nums中的每个元素看作是[nums[i]-k, nums[i]+k]闭区间
# 因此，我们需要选出若干闭区间，这些区间的交集不为空。
# 我们需要找到一批闭区间，这批闭区间的最左闭区间和最右闭区间的交集不为空（x+k>=y-k==>y-x<=2k)，这时候就可以获取一个长度值
# 结论：本题等价于，排序后找到最长的联系子数组，其最大值减最小值<=2k
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ans=0 # 数组中由相等元素组成的最长子序列的长度
        left=0
        nums.sort()
        for right in range(len(nums)):
            while nums[right]-nums[left]>2*k:
                left+=1
            ans=max(ans, right-left+1)
        return ans
        