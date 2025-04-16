# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：自顶向下求解，通过dfs来求解最小深度

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans=float('inf')
        def dfs(node, cnt):
            if node is None:
                return 
            cnt+=1
            if node.left is None and node.right is None: # node是叶子节点（遇到叶子节点的时候就开始求解其深度）
                nonlocal ans
                ans=min(ans, cnt)
                return 
            dfs(node.left, cnt)
            dfs(node.right, cnt)
        dfs(root, 0)
        return ans