# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = ListNode()
        root.next = head
        
        cur = root
        for i in range(left):
            cur = cur.next
        second = cur
        for i in range(right - left):
            cur = cur.next
        x = cur
        cur = cur.next
        third = cur
        x.next = None
        
        nh = None
        def reverse(node):
            nonlocal nh
            if not node.next:
                nh = node
                return node
            tail = reverse(node.next)
            tail.next = node
            return node
        
        reverse(second)
        
        cur = root
        for i in range(left - 1):
            cur = cur.next
        cur.next = nh
        
        second.next = third
        return root.next
        
        