class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn, mx = 1e9, -1e9
        for i in range(len(nums)):
            if nums[i] < mn:
                mni = i
                mn = nums[i]
            if nums[i] > mx:
                mxi = i
                mx = nums[i]
        a = min(mni, mxi)
        b = max(mni, mxi)
        return min(b+1, len(nums)-a, a+1 + len(nums)-b)