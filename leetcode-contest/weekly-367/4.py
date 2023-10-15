class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        MOD = 12345
        
        ret = [[None for _ in range(C)] for _ in range(R)]
        
        pf = [1] * (R*C)
        for i in range(1, R*C):
            pf[i] = pf[i-1] * grid[(i-1)//C][(i-1)%C] % MOD
                
        
        sf = [1] * (R*C)
        for i in range(R*C-2, -1, -1):
            sf[i] = sf[i+1] * grid[(i+1)//C][(i+1)%C] % MOD
                
        for i in range(R*C):
            ret[i//C][i%C] = pf[i] * sf[i] % MOD
            
        return ret