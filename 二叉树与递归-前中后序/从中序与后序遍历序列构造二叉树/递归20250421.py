# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder)==0:
            return None

        # 构建根节点
        root=TreeNode(postorder[-1])

        # 找到该根节点在中序遍历的数组中的索引
        mid=inorder.index(postorder[-1])
        # 构建左子树
        root.left=self.buildTree(inorder[:mid], postorder[:mid])
        # 构建右子树
        root.right=self.buildTree(inorder[mid+1:], postorder[mid:-1])
        return root
