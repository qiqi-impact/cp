class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        N = len(edges) + 1
        g = [[] for _ in range(N)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        coins = [0] * N
        
        def dfs(idx, q):
            ret = 0
            p, n = [], []
            if cost[idx] >= 0:
                p.append(cost[idx])
            else:
                n.append(cost[idx])
            ct = 1
            for x in g[idx]:
                if x != q:
                    a, b = dfs(x, idx)
                    p += a
                    n += b
                    ct += len(a) + len(b)
            
            p.sort(reverse=True)
            n.sort()
            
            p = p[:3]
            n = n[:3]
            
                    
            if ct < 3:
                ret = 1
                
            else:
                for i in range(4):
                    if not (i <= len(p) and (3-i) <= len(n)):
                        continue
                    pr = 1
                    for j in range(i):
                        pr *= p[j]
                    for j in range(3-i):
                        pr *= n[j]
                    ret = max(ret, pr)
            coins[idx] = ret
            return p, n
        
        dfs(0, -1)
        return coins