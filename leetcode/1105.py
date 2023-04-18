class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def dp(idx):
            if idx == len(books):
                return 0
            t = 0
            mx = 0
            ret = inf
            for i in range(idx, len(books)):
                x, y = books[i]
                t += x
                if t > shelfWidth:
                    break
                mx = max(mx, y)
                ret = min(ret, mx + dp(i+1))
            return ret
        return dp(0)