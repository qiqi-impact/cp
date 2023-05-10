class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges)+1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        dist = [inf for _ in range(n)]
        bobdist = [inf for _ in range(n)]
        path = []
        def dfs(node, depth):
            path.append(node)
            if node == bob:
                for i in range(len(path)):
                    bobdist[path[i]] = len(path)-1-i
            dist[node] = depth
            for x in g[node]:
                if dist[x] == inf:
                    dfs(x, depth+1)
            path.pop()
        dfs(0, 0)

        for i in range(n):
            if dist[i] == bobdist[i]:
                amount[i] //= 2
            elif dist[i] > bobdist[i]:
                amount[i] = 0

        ret = -inf
        def dfs2(node, p, sofar):
            nonlocal ret
            sofar += amount[node]
            isleaf = True
            for x in g[node]:
                if x != p:
                    dfs2(x, node, sofar)
                    isleaf = False
            if isleaf:
                ret = max(ret, sofar)
        dfs2(0, -1, 0)
        return ret
