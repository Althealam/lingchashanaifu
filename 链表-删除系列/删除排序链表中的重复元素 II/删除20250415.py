# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 分析：本题需要dummy_node，因为本题可能会删除头节点
# 思路：让cur从dummy_node开始遍历
# 每次用cur遍历时检查cur.next的值和cur.next.next的值
# 如果cur.next的值和cur.next.next的值相同，则做删除节点的操作（删除掉这两个重复节点）

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node=ListNode(next=head)
        cur=dummy_node
        while cur.next and cur.next.next:
            val=cur.next.val
            if cur.next.next.val==val:
                while cur.next and cur.next.val==val: # 遍历删除掉重复的节点
                    cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy_node.next

        