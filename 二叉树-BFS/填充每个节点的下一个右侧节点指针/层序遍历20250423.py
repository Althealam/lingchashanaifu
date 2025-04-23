"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 思路：层序遍历，在单层遍历的时候记录一下本层的头部节点，然后在遍历的时候让前一个节点指向本节点即可

# 时间复杂度：O(n)
# 空间复杂度：O(n) 取决于队列queue中存储的数量，在层序遍历的过程中，队列最多会存储二叉树某一层所有的节点

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue=collections.deque([root])
        while queue:
            prev=None
            for _ in range(len(queue)):
                node=queue.popleft()
                if prev:
                    prev.next=node
                prev=node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root