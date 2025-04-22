# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)，其中n为二叉树的节点个数
# 空间复杂度：O(n)，满二叉树（每一层都填满）最后一层大概有n/2个节点，因此队列中最多有O(n)个元素

# 思路：BFS这颗二叉树，先将右子树入队，再将左子树入队，这样最后一个出队的就是左下角的节点值了

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        while q:
            node=q.popleft()
            if node.right: 
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val