# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前序遍历：中左右 
# 后序遍历：左右中
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        # 构建根节点
        root=TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        # 左节点
        node=preorder[1]
        # 找到左节点在后序遍历的索引（相当于左子树的长度为index+1，因为数组的下标为i的时候，这个元素是在数组的第i+1个位置）
        index=postorder.index(node)
        # 构建左子树
        root.left=self.constructFromPrePost(preorder[1:index+2], postorder[:index+1])
        # 构建右子树
        root.right=self.constructFromPrePost(preorder[index+2:], postorder[index+1:-1])
        return root
