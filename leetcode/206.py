# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        prv = None
        cur = head
        nx = head.next
        cur.next = None
        while nx:
            prv, cur, nx = cur, nx, nx.next
            cur.next = prv
        return cur