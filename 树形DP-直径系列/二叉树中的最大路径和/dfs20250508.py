# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：
# 空节点的最大贡献值为0
# 非空节点的最大贡献值等于节点值与其子节点的最大贡献值之和（对于叶子节点而言，其最大贡献值等于节点值，相当于子节点的贡献值为0）
# dfs用于获取每个节点的最大贡献值，而ans为最大路径和，取决于该节点的值和该节点的左右子节点的最大贡献值

# 时间复杂度：O(n)，其中n是二叉树的节点个数
# 空间复杂度：O(N)，空间复杂度取决于递归调用层数，最大层数等于二叉树的高度，最坏情况下二叉树的高度等于二叉树中的节点个数

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=float('-inf') # 记录最大路径和
        def dfs(node):
            """
            获取每个节点的最大贡献值
            """
            if node is None:
                return 0 # 没有节点，和为0

            # 计算左右子节点的贡献值
            # 只有当最大贡献值大于0的时候才会选取对应的子节点
            l_val=max(dfs(node.left), 0) # 左子树的链最大和
            r_val=max(dfs(node.right), 0) # 右子树的链最大和

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献
            val=node.val+l_val+r_val

            # 更新答案
            nonlocal ans
            ans=max(ans, val)

            # 返回该节点的最大贡献值
            return max(l_val, r_val)+node.val
        dfs(root)
        return ans
        