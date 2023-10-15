class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mx = -inf
        mxi = None
        mn = inf
        mni = None
        for i in range(len(nums)):
            if i >= indexDifference:
                v = nums[i-indexDifference]
                if v > mx:
                    mx = v
                    mxi = i-indexDifference
                if v < mn:
                    mn = v
                    mni = i-indexDifference
            if mx - nums[i] >= valueDifference:
                return [mxi, i] 
            if nums[i] - mn >= valueDifference:
                return [mni, i]
        return [-1, -1]