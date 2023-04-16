class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        ct = [0] * n
        
        def dfs(node, p, tgt):
            if tgt == node:
                ct[node] += 1
                return True
            for o in g[node]:
                if o != p:
                    if dfs(o, node, tgt):
                        ct[node] += 1
                        return True
            return False
        
        for x, y in trips:
            dfs(x, -1, y)
        
        @cache
        def f(node, p, op):
            ret = price[node] * ct[node]
            for o in g[node]:
                if o != p:
                    ret += f(o, node, True)
            if op:
                v = price[node]//2 * ct[node]
                for o in g[node]:
                    if o != p:
                        v += f(o, node, False)
                ret = min(ret, v)
            return ret
        
        return f(0, -1, True)
                