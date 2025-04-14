# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            # 如果快慢指针相遇了，则返回True
            if fast==slow:
                return True
        return False