# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 后序遍历
# 1. 祖先的定义：如果节点p在root的左右子树中，或者p=root，那么root是p的祖先
# 2. 最近公共祖先的定义：假设节点root为节点p,q的某公共祖先，若其左子节点root.left和右子节点root.right都不是p,q的公共祖先，则称root是最近的公共祖先

# 终止条件：当越过叶节点，则直接返回Null；当root等于p, q，则直接返回root
# 递推工作：开始递归左子节点，返回值记为left；开始递归右子节点，返回值记为right
# 返回值：根据left和right，可以展开四种情况：
# 1. left和right同时为空：说明root的左/右子树都不包含p, q，返回Null
# 2. left和right同时不为空：说明p,q分别在root的两侧，则root为p,q的最近公共祖先
# 3. left为空，right不为空：p,q都不在root的左子树中，直接返回right
# 4. left不为空，right为空：p,q都不在root的右子树中，直接返回left

# 时间复杂度：O(n)，其中n为二叉树的节点数，最坏情况下，需要递归遍历树的所有节点
# 空间复杂度：O(n)，最坏情况下递归深度到达n，因此系统需要使用O(n)的空间

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 空节点
        if root is None:
            return root
        # 遇到p,q节点
        if root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left, p, q) # 左
        right=self.lowestCommonAncestor(root.right, p, q) # 右
        # 中
        if left is None: # 左边为空，则返回right
            return right
        if right is None: # 右边为空，则返回left
            return left
        return root


        