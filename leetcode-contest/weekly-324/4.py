class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        @cache
        def skips(a, b):
            if a == b:
                return 1
            if a < b:
                return skips(b, a)
            return 1 + skips(b, a//2)
        return [skips(a, b) for (a, b) in queries]