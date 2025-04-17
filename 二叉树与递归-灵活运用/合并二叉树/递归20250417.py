# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 原问题：合并二叉树
# 子问题：将二叉树的左右子树进行合并
# 本题是先序遍历，先处理中节点，再处理左右孩子节点

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is not None:
            return root2
        if root1 is not None and root2 is None:
            return root1
        if root1 is None and root2 is None:
            return None
        if root1 is not None and root2 is not None:
            root1.val+=root2.val

        root1.left=self.mergeTrees(root1.left, root2.left)
        root1.right=self.mergeTrees(root1.right, root2.right)
        return root1
        
        