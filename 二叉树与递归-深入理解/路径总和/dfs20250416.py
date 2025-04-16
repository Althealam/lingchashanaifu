# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 从targetSum开始，不断的减去路径上的节点值，如果走到叶子节点时发现targetSum为0，说明找到了一条符合要求的路径
# 1. 如果root为空，则直接返回False
# 2. 将targetSum减去root的值
# 3. 如果root是叶子节点，判断是否targetSum=0
# 4. 递归左子树和右子树

# 时间复杂度：O(n) 每个节点都遍历了一次
# 空间复杂度：O(n) 最坏情况下栈存储了所有节点

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans=[] # 计算每条由根节点到叶子节点的路径总和

        def dfs(node, cnt):
            """
            求解由根节点到叶子节点的路径总和
            """
            if node is None:
                return 
            cnt+=node.val
            if node.left is None and node.right is None: # 遇到了叶子节点
                self.ans.append(cnt)
                cnt-=node.val # 回溯
                return 
            dfs(node.left, cnt)
            dfs(node.right, cnt)

        dfs(root, 0)
        return targetSum in self.ans