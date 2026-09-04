# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Node:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val <= other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        heap = []
        res = ListNode(-1)
        curr = res

        for head in lists:
            if head:
                heappush(heap, Node(head.val, head.next))
        
        while heap:
            node = heappop(heap)
            if node.next:
                heappush(heap, Node(node.next.val, node.next.next))
            curr.next = ListNode(node.val)
            curr = curr.next
        
        return res.next
            


        