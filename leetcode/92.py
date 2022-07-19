# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left -= 1
        right -= 1
        l = []
        cur = head
        for i in range(right+1):
            if i >= left:
                l.append(cur.val)
            cur = cur.next
        l = l[::-1]
        cur = head
        for i in range(right+1):
            if i >= left:
                cur.val = l[i - left]
            cur = cur.next
        return head