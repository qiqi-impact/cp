class Solution:
    def canCross(self, stones: List[int]) -> bool:
        tgt = max(stones)
        ss = set(stones)
        if 1 not in ss:
            return False
        @cache
        def dp(x, k):
            if x == tgt:
                return True
            for t in range(k-1, k+2):
                if t > 0 and x+t in ss:
                    if dp(x+t, t):
                        return True
            return False
        return dp(1, 1)