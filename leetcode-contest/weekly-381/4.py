class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x == y or abs(x - y) == 1:
            ret = []
            for i in range(n):
                ret.append(2 * (n-1-i))
            return ret
        ret = [0] * n
        x -= 1
        y -= 1
        x, y = min(x, y), max(x, y)
        
        def bfs(src):
            d = {src: 0}
            q = deque([src])
            while q:
                t = q.popleft()
                l = [t-1, t+1]
                if t == x:
                    l.append(y)
                if t == y:
                    l.append(x)
                for v in l:
                    if x <= v <= y and v not in d:
                        d[v] = d[t] + 1
                        q.append(v)
            return d
        
        A = bfs(x)
        A = Counter(A.values())
        
        ev = [0] * n
        for k in A:
            if k:
                v = A[k]
                ev[k] += 2*v
                ev[k+x] -= 2*v
        cur = 0
        for i in range(n):
            cur += ev[i]
            ret[i] += cur
        
        ev = [0] * n
        for k in A:
            if k:
                v = A[k]
                ev[k] += 2*v
                ev[k+(n-1-y)] -= 2*v
        cur = 0
        for i in range(n):
            cur += ev[i]
            ret[i] += cur
        
        for k in A:
            if k:
                ret[k-1] += A[k] * (y - x + 1)
        
        z = n - (y - x)
        for i in range(z):
            ret[i] += 2 * (z-i)
            
        for i in range(x+1):
            ret[i] -= 2
            
        for i in range(n-y):
            ret[i] -= 2
        ret[0] += 2
        
        return ret