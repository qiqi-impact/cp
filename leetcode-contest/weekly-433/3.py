class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        @cache
        def dp(i, l, r):
            if i * 2 >= n:
                return 0
            ret = inf
            for j in range(3):
                if j != l:
                    for k in range(3):
                        if k != j and k != r:
                            c = cost[i][j] + cost[n-1-i][k]
                            if i == n-1-i:
                                c = cost[i][j] if j != k else inf
                            ret = min(ret, c + dp(i+1, j, k))
            return ret
        return dp(0, -1, -1)