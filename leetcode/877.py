class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def value(i, j):
            if i == j:
                return piles[i]
            return max(piles[i] - value(i+1, j), piles[j] - value(i, j-1))
        return value(0, len(piles)-1)