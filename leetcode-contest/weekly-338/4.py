class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:        
        n = len(coins)
        if n <= 2:
            return 0
        deg = [0] * n
        g = [set() for _ in range(n)]
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
            deg[x] += 1
            deg[y] += 1
            
        def deledge(x, y):
            g[x].discard(y)
            g[y].discard(x)
            deg[x] -= 1
            deg[y] -= 1
            
        q = deque()
        for i in range(n):
            if deg[i] == 1 and not coins[i]:
                q.append(i)
                
        while q:
            cur = q.popleft()
            if deg[cur] == 1:
                for nx in list(g[cur]):
                    deledge(cur, nx)
                    if deg[nx] == 1 and not coins[nx]:
                        q.append(nx)
        
        l = []
        for i in range(n):
            if deg[i] == 1:
                l.append(i)
        # print(l)
        
        for i in range(2):
            nl = []
            for cur in l:
                if deg[cur] == 1:
                    for nx in list(g[cur]):
                        deledge(cur, nx)
                        if deg[nx] == 1:
                            nl.append(nx)
            l = nl
            # print(l)
        
        return sum(deg)