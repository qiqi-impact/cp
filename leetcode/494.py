class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = defaultdict(int)
        #d[k] = number of ways to get a sum of k (so far in the array)
        d[0] = 1
        for n in nums:
            nd = defaultdict(int)
            for k in [n, -n]:
                for q in d:
                    nd[q+k] += d[q]
            d = nd
        return d[target]