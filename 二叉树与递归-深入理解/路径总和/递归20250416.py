# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 从targetSum开始，不断的减去路径上的节点值，如果走到叶子节点时发现targetSum为0，说明找到了一条符合要求的路径
# 1. 如果root为空，则直接返回False
# 2. 将targetSum减去root的值
# 3. 如果root是叶子节点，判断是否targetSum=0
# 4. 递归左子树和右子树

# 时间复杂度：O(n) 每个节点都遍历了一次
# 空间复杂度：O(n) 最坏情况下栈存储了所有节点

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum-=root.val
        if root.left is None and root.right is None:
            # 遇到叶子节点的时候，则判断是否满足路径和为targetSum
            return targetSum==0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        
        
        