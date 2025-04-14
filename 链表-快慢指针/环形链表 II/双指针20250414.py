# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 分析：
# 头节点到环的入口的距离为a；环的入口到相遇节点的距离为b；相遇节点再到环的入口的距离为c
# 环长=b+c；慢指针移动距离：a+b；快指针移动距离：a+b+k(b+c)
# 由于快指针移动的距离是慢指针移动的两倍，因此2(a+b)=a+b+k(b+c)
# 因此：a-c=(k-1)(b+c)==>a=(k-1)(b+c)+c（head到达入口的距离，相当于从相遇点出发转几圈后再走c步的距离）
# slow从相遇点出发，head从头节点出发，走c步后，slow在入口，head到入口的距离恰好是环长的倍数，继续走，两者必然会在入口相遇

# 时间复杂度：O(n) 慢指针在相遇之前和相遇之后都走了O(n)步
# 空间复杂度：O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow: # 快慢指针相遇时，让slow从相遇点出发，同时head从头节点出发
                while slow is not head: # slow和head相遇的地方一定是环的入口
                    slow=slow.next
                    head=head.next
                return slow # 到达环的入口
        return None # 没有环的入口
        