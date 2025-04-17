# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(node, depth):
            if node is None:
                return 
            if depth==len(ans): # 这个深度首次遇到
                ans.append(node.val)
            dfs(node.right, depth+1) # 先递归右子树，保证首次遇到的一定是最右边的节点
            dfs(node.left, depth+1) # 递归左子树
        dfs(root, 0)
        return ans