class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        MOD = 12345
        
        pr = []
        for i in range(R):
            cur = 1
            for j in range(C):
                cur *= grid[i][j]
                cur %= MOD
            pr.append(cur)
        
            
        lpr = [1] * R
        for i in range(1, R):
            lpr[i] = lpr[i-1] * pr[i-1] % MOD
        
        
        rpr = [1] * R
        for i in range(R-2, -1, -1):
            rpr[i] = rpr[i+1] * pr[i+1] % MOD
            
        
        ret = [[None for _ in range(C)] for _ in range(R)]
        for i in range(R):
            cur = lpr[i] * rpr[i] % MOD
            
            lpc = [1] * C
            for q in range(1, C):
                lpc[q] = lpc[q-1] * grid[i][q-1] % MOD
            rpc = [1] * C
            for q in range(C-2, -1, -1):
                rpc[q] = rpc[q+1] * grid[i][q+1] % MOD
            
            for j in range(C):
                ret[i][j] = cur * lpc[j] * rpc[j] % MOD
        return ret
                
                
                
                
                
        