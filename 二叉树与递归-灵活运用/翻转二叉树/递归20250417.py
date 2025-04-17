# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 原问题：将二叉树进行翻转
# 子问题：将二叉树的左右子树进行翻转
# 本题应该使用后序遍历，先将左右孩子节点进行翻转，然后再翻转根节点

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        left=self.invertTree(root.left) # 翻转左子树
        right=self.invertTree(root.right) # 翻转右子树
        # 中节点
        root.left=right # 交换左右孩子
        root.right=left 
        return root
        