class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        cc = [i for i in range(n)]
        ret = n
        def root(x):
            if cc[x] != x:
                cc[x] = root(cc[x])
            return cc[x]
        def join(x, y):
            nonlocal ret
            rx, ry = root(x), root(y)
            if rx != ry:
                ret -= 1
                cc[rx] = ry
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    join(i, j)
        return ret