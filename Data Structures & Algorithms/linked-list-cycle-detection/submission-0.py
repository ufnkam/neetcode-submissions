# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        l, r = head, head
        while r is not None and r.next is not None:
            l = l.next
            r = r.next.next
            if l == r: return True
        return False