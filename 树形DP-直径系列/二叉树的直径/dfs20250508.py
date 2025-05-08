# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 定义：
# 链：从子树中的叶子节点到当前节点的路径。空节点的链长为-1，叶子节点的链长为0
# 直径：等价于由两条链拼接成的路径。
# 我们枚举每个node，假设直径在这里拐弯，也就是计算由左右两条从下面的叶子节点到node的链的节点值之和，去更新答案的最大值

# 思路：在当前节点拐弯的直径长度=左子树的最长链+右子树的最长链+2（当前节点到这两条链的边）
# 返回给父节点的是以当前节点为根的子树的最长链=max(左子树的最长链, 右子树的最长链)+1
# 比如当二叉树为[1, 2, 3, 4, 5]的时候，左子树的最长链为2，右子树的最长链为0，因此以1为根节点的子树的最长链为2+1=3

# 时间复杂度：O(n)
# 空间复杂度：O(n)，最坏情况下二叉树退化为一条链，递归需要O(n)的栈空间

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node):
            if node is None: # 空节点的链长为-1，叶子节点的链长为0
                return -1
            l_len=dfs(node.left)+1 # 左子树最长链长+1（这里+1是因为包含根节点到该节点的链）
            r_len=dfs(node.right)+1 # 右子树最长链长+1
            nonlocal ans
            ans=max(ans, l_len+r_len) # 两条链拼接成路径
            return max(l_len, r_len) # 当前子树的最大链长
            # dfs返回的是链的长度
        dfs(root)
        return ans
        