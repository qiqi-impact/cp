class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        ct = Counter(nums)
        ret = 0
        for x in ct:
            if ct[x] % k == 0:
                ret += x * ct[x]
        return ret