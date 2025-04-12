# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head # 目前正在遍历的节点
        pre=None # 上一个节点
        while cur: 
            nxt=cur.next # 暂存下一个节点
            cur.next=pre # 将cur指向上一个节点
            pre=cur # 移动pre到cur
            cur=nxt # 移动cur到nxt
        return pre

        