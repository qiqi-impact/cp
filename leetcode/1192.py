class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        
        g = defaultdict(set)
        rg = defaultdict(set)
        vis = [False] * n
        order = []
        def dfs(i):
            vis[i] = True
            for x in graph[i]:
                if i not in g[x]:
                    g[i].add(x)
                    rg[x].add(i)
                    if not vis[x]:
                        dfs(x)
            order.append(i)
        
        for i in range(n):
            if not vis[i]:
                dfs(i)

        cc = [None] * n
        def dfs2(i, c):
            cc[i] = c
            for x in rg[i]:
                if cc[x] is None:
                    dfs2(x, c)
        c = 0
        for i in order[::-1]:
            if cc[i] is None:
                c += 1
                dfs2(i, c)

        ret = []
        for i in range(n):
            for j in graph[i]:
                if i < j and cc[i] != cc[j]:
                    ret.append([i, j])
        return ret
