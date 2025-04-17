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
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
        if left==None and right!=None: 
            return False
        elif left!=None and right==None:
            return False
        elif left==None and right==None:
            return True
        elif left.val!=right.val:
            return False
        # 不可以加上else: return True

        outside=self.compare(left.left, right.right)
        inside=self.compare(left.right, right.left)
        isSame=outside and inside
        return isSame

        