# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if not root.left and not root.right and root.val == key:
            return None

        prv = root
        cur = root
        d = None
        while cur:
            if cur.val > key:
                prv = cur
                cur = cur.left
                d = 0
            elif cur.val < key:
                prv = cur
                cur = cur.right
                d = 1
            else:
                if not cur.left and not cur.right:
                    if d:
                        prv.right = None
                    else:
                        prv.left = None
                elif cur.left:
                    t = cur.left
                    p = cur
                    while t.right:
                        p = t
                        t = t.right
                    if t == p.left:
                        p.left = t.left
                    else:
                        p.right = t.left
                    cur.val = t.val
                else:
                    t = cur.right
                    p = cur
                    while t.left:
                        p = t
                        t = t.left
                    if t == p.left:
                        p.left = t.right
                    else:
                        p.right = t.right
                    cur.val = t.val
                break
        return root
                    