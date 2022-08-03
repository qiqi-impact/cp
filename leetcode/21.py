# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(None)
        cur = ret
        while list1 or list2:
            if not list1:
                pick = 2
            elif not list2:
                pick = 1
            elif list1.val < list2.val:
                pick = 1
            else:
                pick = 2
            if pick == 1:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        return ret.next