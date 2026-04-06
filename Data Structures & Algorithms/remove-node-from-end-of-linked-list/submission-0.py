# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy.next
        prev_remove = dummy
        remove_node = dummy.next
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            prev_remove = remove_node
            remove_node = remove_node.next
        next_remove = remove_node.next
        prev_remove.next = next_remove
        return dummy.next
        
        