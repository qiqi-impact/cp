"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

def pll(node):
    ret = []
    while node:
        ret.append(node.val)
        node = node.next
    return ret

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        r1 = Node(0)
        r1.next = head

        r2 = Node(0)
        p2 = r2

        c1 = head
        while c1:
            nx = c1.next
            c2 = Node(c1.val)
            p2.next = c2

            c2.random = c1.random
            c1.next = c2

            c1 = nx
            p2 = c2

        c2 = r2.next
        while c2:
            if c2.random:
                c2.random = c2.random.next
            c2 = c2.next
        
        return r2.next