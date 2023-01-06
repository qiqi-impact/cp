class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zc = 0
        oc = sum(nums)
        mx = oc + zc
        mxi = [0]
        for i, n in enumerate(nums):
            if n == 0:
                zc += 1
            else:
                oc -= 1
            cur = oc + zc
            if cur > mx:
                mx = cur
                mxi = [i+1]
            elif cur == mx:
                mxi.append(i+1)
        return mxi