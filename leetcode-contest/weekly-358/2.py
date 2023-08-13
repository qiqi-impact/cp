# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        cur = head
        while cur:
            l.append(cur)
            cur = cur.next
        c = 0
        for i in range(len(l)-1, -1, -1):
            x = c + l[i].val*2
            c, l[i].val = x//10, x%10
        if c:
            n = ListNode(c)
            n.next = head
            return n
        return head