class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cc = {}
        def root(x):
            if cc[x] != x:
                cc[x] = root(cc[x])
            return cc[x]
        def join(x, y):
            rx, ry = root(x), root(y)
            if rx != ry:
                cc[rx] = ry
            return rx != ry
        for x, y in edges:
            if x not in cc:
                cc[x] = x
            if y not in cc:
                cc[y] = y
            if not join(x, y):
                return [x,y]