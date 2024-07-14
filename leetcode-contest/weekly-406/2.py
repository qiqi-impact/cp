# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(None)
        root.next = cur = head
        tail = root
        s = set(nums)
        while cur:
            if cur.val in s:
                cur = cur.next
            else:
                tail.next = cur
                tail = cur
                cur = cur.next
                tail.next = None
        return root.next