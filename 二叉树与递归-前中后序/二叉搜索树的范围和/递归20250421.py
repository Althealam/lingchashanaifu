# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)（遍历二叉树的所有节点）
# 空间复杂度：O(n)（递归调用栈的空间。最坏情况下，二叉树退化为链表，此时为O(n)，最好情况下二叉树是平衡的，此时为O(logn)）

class Solution:
    def __init__(self):
        self.result=0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val<=high and root.val>=low:
            self.result+=root.val
        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)
        return self.result
        