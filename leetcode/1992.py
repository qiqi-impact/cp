class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ret = []
        R, C = len(land), len(land[0])
        for i in range(R):
            for j in range(C):
                if land[i][j]:
                    for k in range(i, R+1):
                        if k == R or land[k][j] != 1:
                            mxi = k-1
                            break
                    for l in range(j, C+1):
                        if l == C or land[i][l] != 1:
                            mxj = l-1
                            break
                    ret.append([i, j, mxi, mxj])
                    for a in range(i, mxi+1):
                        for b in range(j, mxj+1):
                            land[a][b] = 0
        return ret