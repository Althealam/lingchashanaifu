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
    def inorder_traversal(self, root):
        res=[]
        self.dfs(res, root)
        return res

    def dfs(self, res, node):
        if node is None:
            return []
        self.dfs(res, node.left)
        res.append(node.val)
        self.dfs(res, node.right)
        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=self.inorder_traversal(root)
        return res[k-1]

        