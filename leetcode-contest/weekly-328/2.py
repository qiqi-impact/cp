class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        df = [[0 for _ in range(n)] for _ in range(n)]
        for a, b, c, d in queries:
            df[a][b] += 1
            if c+1 < n:
                df[c+1][b] -= 1
            if d+1 < n:
                df[a][d+1] -= 1
            if c+1 < n and d+1 < n:
                df[c+1][d+1] += 1
        row = [0] * n
        ret = []
        for i in range(n):
            cur = []
            st = 0
            for j in range(n):
                st += df[i][j]
                cur.append(row[j] + st)
            ret.append(cur)
            row = cur
        return ret