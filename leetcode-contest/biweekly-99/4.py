class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        sg = set()
        for x, y in guesses:
            sg.add((x, y))
            
        v = {}
        
        def dfs(idx, p):
            for o in g[idx]:
                if o != p:
                    dfs(o, idx)
                    if (idx, o) in sg:
                        v[(idx, o)] = 1
                    if (o, idx) in sg:
                        v[(o, idx)] = 0
        dfs(0, -1)
                        
        cur = sum(v.values())
        ret = 0
        def rdfs(idx, p):
            nonlocal ret, cur
            if cur >= k:
                ret += 1
            for o in g[idx]:
                if o != p:
                    if (idx, o) in sg:
                        cur -= 1
                    if (o, idx) in sg:
                        cur += 1
                    rdfs(o, idx)
                    if (idx, o) in sg:
                        cur += 1
                    if (o, idx) in sg:
                        cur -= 1
        rdfs(0, -1)
        return ret
                