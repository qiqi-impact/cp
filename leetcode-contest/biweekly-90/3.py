class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        d = defaultdict(int)
        mxv = 0
        for n in nums:
            d[n%space] += 1
            mxv = max(mxv, d[n%space])
        ret = 1e9
        for n in nums:
            if d[n%space] == mxv:
                ret = min(ret, n)
        return ret