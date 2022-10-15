class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        for i in range(32):
            if n & (1 << i):
                powers.append(i)
        pp = [0]
        for p in powers:
            pp.append(pp[-1] + p)
        ret = []
        for x, y in queries:
            ret.append(pow(2, pp[y+1] - pp[x], 10**9+7))
        return ret