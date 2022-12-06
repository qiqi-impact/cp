# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = 1
        
        odds = ListNode()
        evens = ListNode()
        
        curodd = odds
        cureven = evens
        
        while head:
            if cur%2:
                curodd.next = head
                head = head.next
                curodd = curodd.next
                curodd.next = None
            else:
                cureven.next = head
                head = head.next
                cureven = cureven.next
                cureven.next = None
            cur += 1
            
        curodd.next = evens.next
        return odds.next