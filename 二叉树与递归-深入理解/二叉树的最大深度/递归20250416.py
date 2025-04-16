# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 最大深度是根节点到最远的叶子节点的距离
# 整棵树的最大深度=max(左子树的最大深度,右子树的最大深度)+1
# 1. 原问题：计算整棵树的最大深度
# 2. 子问题：计算左/右子树的最大深度
# 类比循环，执行的代码也应该是相同的。但是子问题需要将计算结果返回给上一级问题，因此更适合用递归实现。

# 时间复杂度：O(n) 每个节点都被遍历了一次
# 空间复杂度：O(n)
# 递归需要用到栈，最坏的情况是假设只有左孩子没有右孩子，此时二叉树变成了链表，那么栈的大小就变成了O(n)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        return max(left_depth, right_depth)+1