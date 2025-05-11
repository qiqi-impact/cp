class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        row = [0] * R
        col = [0] * C
        tot = 0
        for i in range(R):
            for j in range(C):
                tot += grid[i][j]
                row[i] += grid[i][j]
                col[j] += grid[i][j]
        prow = [0]
        for i in range(R):
            prow.append(prow[-1] + row[i])
        pcol = [0]
        for i in range(C):
            pcol.append(pcol[-1] + col[i])

        if R == 1 and C == 1:
            return False

        if R == 1:
            cur = 0
            for j in range(C):
                cur += grid[0][j]
                if cur == tot - cur or cur - grid[0][0] == tot - cur or cur - grid[0][j] == tot - cur:
                    return True
            cur = 0
            for j in range(C-1, -1, -1):
                cur += grid[0][j]
                if cur == tot - cur or cur - grid[0][-1] == tot - cur or cur - grid[0][j] == tot - cur:
                    return True
            return False

        if C == 1:
            cur = 0
            for i in range(R):
                cur += grid[i][0]
                if cur == tot - cur or cur - grid[0][0] == tot - cur or cur - grid[i][0] == tot - cur:
                    return True
            cur = 0
            for i in range(R-1, -1, -1):
                cur += grid[i][0]
                if cur == tot - cur or cur - grid[-1][0] == tot - cur or cur - grid[i][0] == tot - cur:
                    return True
            return False

        s = defaultdict(int)
        sm = 0
        for i in range(R):
            for j in range(C):
                s[grid[i][j]] += 1
                sm += grid[i][j]
            if i == 0:
                for j in range(1, C-1):
                    s[grid[i][j]] -= 1
            cur = sm
            other = tot - cur
            if s[cur - other] > 0 or cur == other:
                return True
            if i == 0:
                for j in range(1, C-1):
                    s[grid[i][j]] += 1
        
        s = defaultdict(int)
        sm = 0
        for i in range(R-1, -1, -1):
            for j in range(C):
                s[grid[i][j]] += 1
                sm += grid[i][j]
            if i == R-1:
                for j in range(1, C-1):
                    s[grid[i][j]] -= 1
            cur = sm
            other = tot - cur
            if s[cur - other] > 0 or cur == other:
                return True
            if i == R-1:
                for j in range(1, C-1):
                    s[grid[i][j]] += 1

        s = defaultdict(int)
        sm = 0
        for j in range(C):
            for i in range(R):
                s[grid[i][j]] += 1
                sm += grid[i][j]
            if j == 0:
                for i in range(1, R-1):
                    s[grid[i][j]] -= 1
            cur = sm
            other = tot - cur
            if s[cur - other] > 0 or cur == other:
                return True
            if j == 0:
                for i in range(1, R-1):
                    s[grid[i][j]] += 1

        s = defaultdict(int)
        sm = 0
        for j in range(C-1, -1, -1):
            for i in range(R):
                s[grid[i][j]] += 1
                sm += grid[i][j]
            if j == C-1:
                for i in range(1, R-1):
                    s[grid[i][j]] -= 1
            cur = sm
            other = tot - cur
            if s[cur - other] > 0 or cur == other:
                return True
            if j == C-1:
                for i in range(1, R-1):
                    s[grid[i][j]] += 1

        return False
                
            
                