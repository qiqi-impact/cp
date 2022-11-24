class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        @cache
        def dp(p):
            if sum(p) == 0:
                return False
            l = list(p)
            for i in range(len(l)):       
                v = l[i]
                for j in range(l[i]):
                    l[i] = j
                    if not dp(tuple(sorted(l))):
                        return True
                    l[i] = v
        return dp(tuple(sorted(piles)))