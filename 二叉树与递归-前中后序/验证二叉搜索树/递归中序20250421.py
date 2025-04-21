# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 将二叉搜索树以中序遍历获取数组，判断该数组是否是递增的

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def __init__(self):
        self.pre=-inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val<=self.pre:
            return False
        self.pre=root.val
        return self.isValidBST(root.right)