class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ret = 0
        for i in range(len(nums)):
            lcm = 1
            for j in range(i, len(nums)):
                lcm = math.lcm(lcm, nums[j])
                if lcm == k:
                    ret += 1
        return ret