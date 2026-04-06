# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0)
        middle = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            middle = middle.next
        curr = middle
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        left = head
        right = prev
        print(prev.val)
        k = 0
        while right and left:
            if k % 2 == 0:
                dummy.next = left
                left = left.next
            else:
                dummy.next = right
                right = right.next

            dummy = dummy.next
            k += 1
        head = dummy.next