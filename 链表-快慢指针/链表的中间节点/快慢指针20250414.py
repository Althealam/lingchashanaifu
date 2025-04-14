# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：定义slow和fast指向链表的头节点
# 每次循环，fast走两步，slow走一步
# 当链表长度为奇数的时候，当fast到链表最后一个节点的时候，slow一定在链表的中间节点
# 当链表长度为偶数的时候，当fast指向空的时候，slow一定在链表的中间节点（第二个中间节点）

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        