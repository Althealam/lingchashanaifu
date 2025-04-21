# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 二叉搜索树：左节点的值小于根节点的值，右节点的值大于根节点的值

# 原问题：判断二叉搜索树
# 子问题：根据根节点的值，获取每个节点的值区间范围，然后判断其左右节点值是否满足该区间范围

# 时间复杂度：O(n)
# 对于这个BST的每个节点，代码都要访问一次，因此遍历完所有节点的时间复杂度为O(n)
# 空间复杂度：O(logn)
# 空间复杂度取决于递归调用栈的深度，最坏情况下二叉搜索树退化为链表，此时递归调用栈的深度为n，空间复杂度为O(n)
# 最好情况下，二叉搜索树是完全平衡的，其高度为logn，递归调用栈的深度是树的高度，此时空间复杂度为O(logn)

class Solution:
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if root is None:
            return True
        x=root.val
        return left<x<right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)
    
        