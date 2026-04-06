# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        mult = 1
        first_number = 0
        second_number = 0
        while l1:
            first_number += l1.val * mult
            mult *= 10
            l1 = l1.next
        mult = 1
        while l2:
            second_number += l2.val * mult
            mult *= 10
            l2 = l2.next
        num_sum = first_number + second_number
        digits = str(num_sum)
        prev = ListNode(int(digits[-1]))
        head = prev
        for i in range(len(digits) - 2, -1, -1):
            node = ListNode(int(digits[i]))
            prev.next = node
            prev = prev.next
        return head
            