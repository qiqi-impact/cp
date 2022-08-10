class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        mxdp = -1
        mxidx = None
        path = []
        mids = []
        def dfs(i, p, dp):
            nonlocal mxdp, mxidx, path, mids
            if dp > mxdp:
                mxdp = dp
                mxidx = i
                mids = [path[mxdp//2]]
                if mxdp%2:
                    mids.append(path[(mxdp+1)//2])
            for ch in g[i]:
                if ch != p:
                    path.append(ch)
                    dfs(ch, i, dp+1)
                    path.pop()
            
        for i in range(n):
            if len(g[i]) <= 1:
                path = [i]
                mids = [i]
                dfs(i, None, 0)
                break
        path = [mxidx]
        mids = [mxidx]
        mxdp = -1
        mxidx = None
        dfs(path[0], None, 0)
        return mids
        