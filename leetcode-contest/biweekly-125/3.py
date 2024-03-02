class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], s: int) -> List[int]:
        n = len(edges)+1
        g = [{} for _ in range(n)]
        for x, y, z in edges:
            g[x][y] = g[y][x] = z%s
            
        
        def dfs(node, p, cur):
            me[node] = int(cur == 0)
            for o in g[node]:
                if o != p:
                    me[node] += dfs(o, node, (cur + g[node][o])%s)
            return me[node]
        
        ret = [0] * n
        for i in range(n):
            me = [0] * n
            dfs(i, -1, 0)
            acc = 0
            for o in g[i]:
                ret[i] += acc * me[o]
                acc += me[o]
        return ret
                    