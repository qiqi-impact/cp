from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict()
        q = deque([(root, 0, 0)])
        while q:
            node, level, depth = q.popleft()
            if level not in d:
                d[level] = defaultdict(list)
            d[level][depth].append(node.val)
            if node.left:
                q.append((node.left, level-1, depth+1))
            if node.right:
                q.append((node.right, level+1, depth+1))
        ret = []
        for k in sorted(d.keys()):
            cur = []
            for x in sorted(d[k].keys()):
                cur += sorted(d[k][x])
            ret.append(cur)
        return ret