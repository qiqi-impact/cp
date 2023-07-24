# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n%2:
            return []

        @cache
        def dp(x):
            if x == 1:
                return '0'
            ret = []
            for i in range(1, x, 2):
                a, b = dp(i), dp(x-1-i)
                for l in a:
                    for r in b:
                        ret.append('({},{})'.format(l, r))
            return ret

        q = []
        for s in dp(n):
            st = []
            for c in s:
                if c == '0':
                    st.append(TreeNode(0))
                elif c == ')':
                    r, l = st.pop(), st.pop()
                    st.append(TreeNode(0, l, r))
            q.append(st[0])
        return q