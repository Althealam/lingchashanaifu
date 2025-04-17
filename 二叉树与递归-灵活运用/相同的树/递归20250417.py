# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 原问题：二叉树是否是相同的
# 子问题：左右子树是否是相同的

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 递归的终止条件为p或者q为空节点
        if p is None or q is None:
            return p is q # 当p和q都为空的时候，才能返回True
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        