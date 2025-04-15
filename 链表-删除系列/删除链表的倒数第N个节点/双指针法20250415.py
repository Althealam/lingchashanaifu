# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 分析：什么时候要用到虚拟头节点dummy_node：当需要删除头节点的时候则需要dummy_node
# 方法：
# 1. 遍历链表，求出链表的长度，由此可以知道倒数第n个节点是正数第k个节点，然后再次从头遍历链表，删除倒数第n个节点即可
# 2. 定义双指针，要删除倒数第n个节点，那么找到倒数第n+1个节点即可。初始化fast，让fast先走n步，slow在dummy_node的位置，然后让fast和slow一起走，此时左右指针的距离始终是n，那么当fast到达最后一个节点时，slow就走到了倒数n+1个节点（也就是倒数第n个节点的前面一个节点）

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node=ListNode(next=head)

        # 初始化fast，让fast和slow的距离为n
        fast=dummy_node
        for _ in range(n):
            fast=fast.next
        # 初始化slow
        slow=dummy_node
        
        # slow指向的是倒数第n个节点的前面一个节点
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy_node.next


        