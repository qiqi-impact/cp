class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        @cache
        def dp(idx, left):
            if left == 0:
                return 0
            ret = 0
            for x in range(n):
                if x == idx:
                    ret = max(ret, stayScore[k-left][x] + dp(idx, left - 1))
                else:
                    ret = max(ret, travelScore[idx][x] + dp(x, left - 1))
            return ret
        return max([dp(i, k) for i in range(n)])