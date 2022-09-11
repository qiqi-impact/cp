class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = defaultdict(int)
        mx = 0
        for n in nums:
            if n%2==0:
                d[n] += 1
                mx = max(mx, d[n])
        mni = 1e9
        for k in d:
            if d[k] == mx:
                mni = min(mni, k)
        return mni if mni != 1e9 else -1