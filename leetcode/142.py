# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = f = head
        while s and f:
            if f.next == None:
                return None
            s = s.next
            f = f.next.next
            if s == f:
                break
        if not f: return None
        a, b = head, s
        while 1:
            if a == b:
                return a
            a = a.next
            b = b.next