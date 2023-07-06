class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        df = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for a, b, c, d in queries:
            df[a][b] += 1
            df[a][d+1] -= 1
            df[c+1][b] -= 1
            df[c+1][d+1] += 1
        
        ret = [[0 for _ in range(n)]]
        for i in range(n):
            cur = ret[-1][:]
            st = 0
            for j in range(n):
                st += df[i][j]
                cur[j] += st
            ret.append(cur)
        return ret[1:]