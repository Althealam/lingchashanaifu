# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 求出链表个数，每次反转前判断剩余个数：如果剩余个数>=k则反转；如果剩余个数<k则不能反转

        # 1. 求解链表长度
        n=0
        cur=head
        while cur:
            n+=1
            cur=cur.next
        
        # 2. 反转链表
        dummy=ListNode(next=head) 
        p0=dummy
        while n>=k: # 判断剩余的节点数是否满足反转条件
            n-=k # 将剩余个数减去k
            pre=None # 当前反转的链表的上一个节点
            cur=p0.next # 当前正在遍历的节点

            # 反转k个节点（反转操作次数为k-1）
            for _ in range(k):
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=nxt
             
            nxt=p0.next 
            p0.next.next=cur # 将反转后的链表和最左边的部分连接起来
            p0.next=pre # 将反转后的链表和右边的部分连接起来
            p0=nxt # 更新p0的值
        return dummy.next




        