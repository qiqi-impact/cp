class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def pullnode(node, k):
    '''
    like: list: 1 2 3 4 and k is 2,
    the final list is 2 3 1 4
    '''
    if k == 0: return node
    root = Node(None)
    root.next = node
    new_head = node.next
    cur = node
    for i in range(k):
        cur = cur.next
        if not cur:
            return node
    node.next = cur.next
    cur.next = node
    root.next = new_head
    return new_head

l = [1, 2, 3, 4]
root = Node(None)
cur = root
for n in l:
    cur.next = Node(n)
    cur = cur.next
root = root.next

r = pullnode(root, 2)
while r:
    print(r.val)
    r = r.next
