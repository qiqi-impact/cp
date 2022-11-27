# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = []
        
        cur = head
        while cur:
            while s and s[-1] < cur.val:
                s.pop()
            s.append(cur.val)
            cur = cur.next
        
        ret = ListNode()
        cr = ret
        for c in s:
            l = ListNode(c)
            cr.next = l
            cr = l
        return ret.next