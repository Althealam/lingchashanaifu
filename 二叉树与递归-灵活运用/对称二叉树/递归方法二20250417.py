# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 原问题：判断二叉树是否是对称的
# 子问题：判断左子树的左子树和右子树的右子树是否是相同的

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left, root.right)

    def compare(self, p, q):
        # 递归的终止条件
        if p is None or q is None:
            return p is q
        return p.val==q.val and self.compare(p.left, q.right) and self.compare(p.right, q.left)
    