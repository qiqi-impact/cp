class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        dst = [[inf for _ in range(n)] for _ in range(n)]
        
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dst[i][j] = 0
        
                
        mx = 0
        while q:
            x, y = q.popleft()
            for dx, dy in pairwise([1,0,-1,0,1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and dst[nx][ny] == inf:
                    dst[nx][ny] = dst[x][y] + 1
                    mx = max(mx, dst[nx][ny])
                    q.append((nx, ny))
                    
                    
        def can(t):
            if dst[0][0] < t:
                return False
            qq = deque([(0, 0)])
            seen = set([(0, 0)])
            while qq:
                x, y = qq.popleft()
                for dx, dy in pairwise([1,0,-1,0,1]):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n and dst[nx][ny] >= t and (nx, ny) not in seen:
                        qq.append((nx, ny))
                        seen.add((nx, ny))
                        if (nx, ny) == (n-1, n-1):
                            return True
            return False
        
        l, r = 0, mx
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l
        
    