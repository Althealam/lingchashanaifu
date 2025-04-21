# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 二叉搜索树的性质是：中序遍历的数组是递增数组（从小到大），选择递增数组的第k-1个

# 空间复杂度：递归调用栈的深度，最坏情况下递归调用栈的深度为树的高度（对于一个包含n个节点的完全平衡的二叉树，其高度为O(logn)），在树退化为链表的时候，递归调用栈的深度为O(n)

# 时间复杂度：O(n)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def middle(root):
            """
            求解中序遍历的数组
            """
            if root is None:
                return []
            return middle(root.left)+[root.val]+middle(root.right)
        ans=middle(root)
        return ans[k-1]

        