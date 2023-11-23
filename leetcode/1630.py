class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ret = []
        for x, y in zip(l, r):
            z = sorted(nums[x:y+1])
            if len(z) <= 2:
                ret.append(True)
            else:
                a = True
                for i in range(1, len(z)-1):
                    if z[i+1] - z[i] != z[1] - z[0]:
                        a = False
                        break
                ret.append(a)
        return ret