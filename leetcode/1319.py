class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cc = list(range(n))
        def root(x):
            if cc[x] != x:
                cc[x] = root(cc[x])
            return cc[x]
        ct = n-1
        cab = 0
        def join(x, y):
            rx = root(x)
            ry = root(y)
            if rx != ry:
                cc[rx] = ry
                return 1
            return 0
        for x, y in connections:
            v = join(x, y)
            if v == 0:
                cab += 1
            else:
                ct -= 1
        return ct if ct <= cab else -1