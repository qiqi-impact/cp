class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        d = {0: 1}
        for x in stones:
            nd = defaultdict(int)
            for k in d:
                nd[k+x] += d[k]
                nd[k-x] += d[k]
            d = nd
        ret = inf
        for k in d:
            if k >= 0:
                ret = min(ret, k)
        return ret