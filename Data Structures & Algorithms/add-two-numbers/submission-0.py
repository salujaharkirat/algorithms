# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        curr = res
        p1 = l1
        p2 = l2
        carry = 0

        while p1 or p2:
            val = carry
            if p1:
                val += p1.val
            if p2:
                val += p2.val

            if val > 9:
                val = val % 10
                carry = 1
            else:
                carry = 0

            curr.next = ListNode(val)
            curr = curr.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if carry:
            curr.next = ListNode(1)
            curr = curr.next
            
        return res.next 

        