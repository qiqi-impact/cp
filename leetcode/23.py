# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = ListNode()
        cur = root
        n = len(lists)
        h = []
        
        for i in range(n):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
        
        while h:
            x, i = heapq.heappop(h)
            node = ListNode(x)
            cur.next = node
            cur = node
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
        return root.next