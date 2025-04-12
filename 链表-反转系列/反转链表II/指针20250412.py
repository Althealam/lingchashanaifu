# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(next=head) # 为了避免出现left=1的情况
        p0=dummy # 用来查找left之前的节点和left，并且用来保存left之前的节点
        
        # 找到left的上一个节点
        for _ in range(left-1):
            p0=p0.next
        
        # 和反转链表是一样的！
        pre=None
        # 找到left节点
        cur=p0.next # 相当于cur=head

        # 反转left到right之间的链表
        for _ in range(right-left+1): # 比如left=2，right=4，则总共要反转2次，也就是for _ in range(3)
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        
        # 将反转后的链表和其他的链表部分连接起来
        # 1. 将反转后的链表和right之后的节点连接起来
        p0.next.next=cur

        # 2. 将反转后的链表和left之前的节点连接起来
        p0.next=pre
        
        return dummy.next

        
