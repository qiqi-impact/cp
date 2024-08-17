class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        R, C = len(board), len(board[0])

        upper = [[None for _ in range(C)] for _ in range(R)]
        lower = [[None for _ in range(C)] for _ in range(R)]

        for i in range(R):
            for j in range(C):
                upper[i][j] = board[i][j]
                if i > 0:
                    upper[i][j] = max(upper[i][j], upper[i-1][j])

        for i in range(R-1, -1, -1):
            for j in range(C):
                lower[i][j] = board[i][j]
                if i < R-1:
                    lower[i][j] = max(lower[i][j], lower[i+1][j])

        def best3(r):
            l = heapq.nlargest(3, [(x, i) for (i, x) in enumerate(r)])
            return l

        U = [best3(r) for r in upper]
        L = [best3(r) for r in lower]

        ret = -inf
        for i in range(1, R-1):
            cur = best3(board[i])
            for a, b in cur:
                for c, d in U[i-1]:
                    if b != d:
                        for e, f in L[i+1]:
                            if f not in [b, d]:
                                ret = max(ret, a + c + e)

        return ret
                            