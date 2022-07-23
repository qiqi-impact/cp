class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = 0
        ret = 0
        for n in nums:
            if n == 0:
                l += 1
            else:
                if l > 0:
                    ret += (l)*(l+1)//2
                l = 0
        if l > 0:
            ret += (l)*(l+1)//2
        return ret