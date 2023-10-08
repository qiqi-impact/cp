v# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = l1, l2
        
        carry = 0
        
        ret = ListNode(None)
        cur = ret

        while a or b or carry:
            v = carry
            if a:
                v += a.val
                a = a.next
            if b:
                v += b.val
                b = b.next
            v, carry = v%10, v//10
            nn = ListNode(v)
            cur.next = nn
            cur = nn
        
        return ret.next