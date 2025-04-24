# 回溯三问：
# 1. 当前操作：枚举path[i]要填入的字母
# 2. 子问题：构造字符串>=i的部分
# 3. 下一个子问题：构造字符串>=i+1的部分

# 子集型回溯：每个元素都可以选/不选

# 时间复杂度：O(n*2**n)
# 1. 总的子集数量：对于一个包含n个元素的数组，每个元素在子集中都有两种状态，因此总的子集数量为2**n个
# 2. 将子集添加到结果列表中，复制子集的操作为O(n)
# 空间复杂度：O(n*)
# 1. 递归调用栈：回溯算法使用递归调用栈来实现dfs，最坏情况下递归的深度为n（即数组的长度），因为每次递归调用都会选择一个元素，直到遍历完所有元素 O(n*2**n)
# 2. 存储结果的空间：需要存储所有的子集，总的子集数量为2**n个，每个子集的长度最大为n，因此为O(n*2**n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        self.traversal(result, path, nums, 0)
        return result
    
    def traversal(self, result, path, nums, startIndex):
        # 子集问题在每个节点都收割结果，因此没有收割条件
        result.append(path[:])
        for i in range(startIndex, len(nums)): # 枚举
            path.append(nums[i])
            self.traversal(result, path, nums, i+1) # 枚举i后面的元素
            path.pop()
