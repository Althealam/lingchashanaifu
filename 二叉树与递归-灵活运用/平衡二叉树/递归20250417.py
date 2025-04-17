# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 原问题：判断二叉树是否是平衡的（左子树和右子树的高度差不超过1）
# 子问题：求解二叉树的高度，如果高度差超过1，那么返回-1

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getheight(root)!=-1
        # 只要返回值不是-1，说明是平衡二叉树，则返回True；如果返回值是-1，说明不是平衡二叉树，则返回False
    
    def getheight(self, root):
        if root is None:
            return 0
        left_height=self.getheight(root.left)
        if left_height==-1:
            return -1
        right_height=self.getheight(root.right)
        if right_height==-1 or abs(left_height-right_height)>1:
            return -1
        return max(left_height, right_height)+1

        