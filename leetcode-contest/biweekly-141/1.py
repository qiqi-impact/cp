class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ret = []
        for x in nums:
            f = 0
            for i in range(x+1):
                if i|i+1 == x:
                    f = 1
                    ret.append(i)
                    break
            if not f:
                ret.append(-1)
        return ret