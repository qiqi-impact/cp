from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([(root, 0)])
        ret = []
        while q:
            x, y = q.popleft()
            if y == len(ret):
                ret.append([])
            ret[-1].append(x.val)
            for ch in x.left, x.right:
                if ch:
                    q.append((ch, y+1))
        for i in range(1, len(ret), 2):
            ret[i] = ret[i][::-1]
        return ret