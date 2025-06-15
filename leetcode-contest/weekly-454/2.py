class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        right = defaultdict(int)
        left = defaultdict(int)
        n = len(nums)
        for i in range(1, n):
            right[nums[i]] += 1
        ret = 0
        MOD = 10**9+7
        for i in range(n - 1):
            v = nums[i]
            ret += left[2*v] * right[2*v]
            ret %= MOD
            left[v] += 1
            right[nums[i+1]] -= 1
        return ret