# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy.next
        group_prev = dummy
        n = 0
        temp = curr
        while temp:
            temp = temp.next
            n += 1
        while curr:
            temp = curr
            count = 0
            while temp and count < k:
                temp = temp.next
                count += 1
            if n - k >= 0:
                prev = None
                node = curr
                for _ in range(count):
                    node_next = node.next
                    node.next = prev
                    prev = node
                    node = node_next
                group_prev.next = prev
                curr.next = node
                group_prev = curr
                curr = node
            else:
                curr = curr.next
            n -= k
        return dummy.next
            

                