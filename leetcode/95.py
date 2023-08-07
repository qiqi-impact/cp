# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def f(l, r):
            ret = []
            for i in range(l, r+1):
                x = [None]
                y = [None]
                if i != l:
                    x = f(l, i-1)
                if i != r:
                    y = f(i+1, r)
                for xx in x:
                    for yy in y:
                        ret.append([i, xx, yy])
            return ret
        
        def decode(v):
            if v is None:
                return None
            node = TreeNode(v[0])
            node.left = decode(v[1])
            node.right = decode(v[2])
            return node

        return [decode(t) for t in f(1, n)]
