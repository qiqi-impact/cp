class Node:
    def __init__(self, val):
        self.left = self.right = None
        self.val = val

def pathtonode(root, val):
    path = []
    def find(node, val):
        if not node:
            return False
        path.append(node.val)
        if node.val == val:
            return True
        for ch in node.left, node.right:
            if find(ch, val):
                return True
        path.pop()
    find(root, val)
    return path

l = [1,2,3,4,5,6]

def fill(idx):
    n = Node(l[idx])
    if 2*idx+1 < len(l):
        n.left = fill(2*idx+1)
    if 2*idx+2 < len(l):
        n.right = fill(2*idx+2)
    return n
r = fill(0)
print(pathtonode(r, 5))
