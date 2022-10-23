class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ret = 0
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i, len(nums)):
                cur = math.gcd(cur, nums[j])
                if cur == k:
                    ret += 1
        return ret