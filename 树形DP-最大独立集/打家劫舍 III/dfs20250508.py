# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 分析：后序遍历，求出每个节点选或者不选的状态下的最大金额
# 1. 选或者不选：如果选当前节点，则左右儿子都不能选；如果不选当前节点，则左右儿子可选可不选
# 2.提炼状态：选当前节点时，以当前节点为根的子树的最大点权和；不选当前节点时，以当前节点为根的子树的最大点权和
# 3. 转移方程
# （1）选=左不选+右不选+当前节点值
# （2）不选=max(左选，左不选)+max(右选，右不选)
# 最终答案=max(根选，根不选)

# 时间复杂度：O(n)，需要遍历每个节点
# 空间复杂度：O(n)，最坏情况下二叉树为链，则是递归需要O(n)的栈空间

# 一般树：选=不选当前子节点之和+当前节点值；不选=max(选子节点， 不选子节点)之和
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            l_rob, l_not_rob=dfs(node.left)
            r_rob, r_not_rob=dfs(node.right)
            rob=l_not_rob+r_not_rob+node.val
            not_rob=max(l_not_rob, l_rob)+max(r_not_rob, r_rob)
            return rob, not_rob
        return max(dfs(root))
        