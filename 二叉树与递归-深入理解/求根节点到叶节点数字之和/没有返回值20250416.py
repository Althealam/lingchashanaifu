# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 更新方法：x=x*10+node.val
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=0 # 求解路径总和
        def dfs(node, path_sum):
            """
            求解根节点到叶子节点的路径的和
            """
            if not node:
                return 
            path_sum=path_sum*10+node.val # 求解目前的路径的和（每当层数加1，就会乘上10）
            # 到达叶子节点时，则将该条路径的和加到ans上
            if node.left is None and node.right is None:
                nonlocal ans 
                ans+=path_sum
                return 
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)
        dfs(root, 0)
        return ans


        