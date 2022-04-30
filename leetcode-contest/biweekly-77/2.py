class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        pfx = [0] * len(nums)
        sfx = [0] * len(nums)
        sfx[-1] = nums[-1]
        pfx[0] = nums[0]
        for i in range(1, len(nums)):
            pfx[i] = pfx[i-1] + nums[i]
        
        for i in range(len(nums)-2, 0, -1):
            sfx[i] = sfx[i+1] + nums[i]
            
        sfx += [0]
        
        ret = 1e9
        idx = None
        for i in range(len(nums)):
            l = pfx[i] // (i+1)
            r = sfx[i+1] // max(1, (len(nums) - (i+1)))
            # print(i, abs(l-r))
            if (abs(l-r) < ret):
                idx = i
                ret = abs(l-r)
        return idx
            
        