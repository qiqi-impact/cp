class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ret = 0
        for i in range(len(nums)):
            lcm = 1
            for j in range(i, len(nums)):
                lcm = lcm * nums[j] // math.gcd(lcm, nums[j])
                if lcm == k:
                    ret += 1
        return ret