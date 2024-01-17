"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            cur = node
            while 1:
                nx = cur.next
                if cur.child:
                    x = dfs(cur.child)
                    cur.next = cur.child
                    x.next = nx
                    cur.next.prev = cur
                    if nx:
                        x.next.prev = x
                    cur.child = None
                    cur = x
                if not cur.next:
                    return cur
                cur = cur.next
        if head: dfs(head)
        return head
