class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        ct = Counter(nums)
        mx = 0
        mxi = None
        for k in sorted(ct.keys()):
            if k%2==0 and mx < ct[k]:
                mx = ct[k]
                mxi = k
        return mxi if mxi is not None else -1