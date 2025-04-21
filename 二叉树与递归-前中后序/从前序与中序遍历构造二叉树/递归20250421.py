# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        :param preorder：先序遍历数组
        :param inorder：中序遍历数组
        """
        if len(inorder)==0:
            return None
        # 前序遍历的第一个值为根节点
        root=TreeNode(preorder[0])

        # 根据中序遍历找到中间节点的索引
        mid=inorder.index(preorder[0])

        # 构建左子树
        root.left=self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 构建右子树
        root.right=self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        