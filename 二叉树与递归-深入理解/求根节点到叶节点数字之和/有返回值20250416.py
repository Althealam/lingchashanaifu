# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n) 每个节点都遍历一次
# 空间复杂度：O(n) 最坏情况下，二叉树退化为一条链，递归需要O(n)的栈空间

# 更新方法：x=x*10+node.val
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], x=0) -> int:
        if root is None:
            return 0
        x=x*10+root.val
        if root.left is None and root.right is None:
            return x
        return self.sumNumbers(root.left, x)+self.sumNumbers(root.right, x)