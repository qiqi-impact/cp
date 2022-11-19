class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        R, C = len(pizza), len(pizza[0])
        A = [[0 for _ in range(C+1)] for _ in range(R+1)]
        
        for i in range(1, R+1):
            for j in range(1, C+1):
                A[i][j] = int(pizza[i-1][j-1] == 'A') + A[i-1][j] + A[i][j-1] - A[i-1][j-1]
        def has_apple(a, b, c, d):
            return bool(A[c+1][d+1] - A[a][d+1] - A[c+1][b] + A[a][b])
        
        @cache
        def dp(i, j, rem):
            if i == R or j == C:
                return 0
            if rem == 1:
                return int(has_apple(i, j, R-1, C-1))
            ret = 0
            for x in range(i+1, R):
                if has_apple(i, j, x-1, C-1):
                    ret += dp(x, j, rem-1)
            for x in range(j+1, C):
                if has_apple(i, j, R-1, x-1):
                    ret += dp(i, x, rem-1)
            return ret%(int(1e9)+7)
        
        return dp(0, 0, k) 