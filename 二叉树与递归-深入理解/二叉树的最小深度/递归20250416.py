# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：后序遍历，自底向上递归遍历
# 1. 如果node是空节点，则直接返回0
# 2. 如果node没有右孩子，则深度为左子树的深度加1
# 3. 如果node没有左孩子，则深度为右子树的深度加1
# 4. 如果左右孩子都有，那么递归计算左右子树的深度，取最小值然后加1

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 情况一：没有右孩子
        if not root.right:
            return self.minDepth(root.left)+1
        # 情况二：没有左孩子
        if not root.left:
            return self.minDepth(root.right)+1
        # 情况三：左右孩子都有
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1