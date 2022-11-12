class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges)+1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        bob_dist = [float('inf')] * n
        def bd(idx, p):
            if idx == bob:
                bob_dist[idx] = 0
            else:
                for ch in g[idx]:
                    if ch != p:
                        v = bd(ch, idx)
                        if v != float('inf'):
                            bob_dist[idx] = 1 + v
                            break
            return bob_dist[idx]
        bd(0, -1)
        
        def dfs(idx, p, depth):
            cur = 0
            if bob_dist[idx] == depth:
                cur = amount[idx]//2
            elif bob_dist[idx] > depth:
                cur = amount[idx]
                
            # print(idx, p, depth, cur)
                
            best = float('-inf')
            has_child = False
            for ch in g[idx]:
                if ch != p:
                    best = max(best, dfs(ch, idx, depth+1))
                    has_child = True
            return (best + cur) if has_child else cur
        return dfs(0, -1, 0)