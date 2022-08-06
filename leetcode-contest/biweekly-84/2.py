class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i, e in enumerate(nums):
            d[e-i] += 1
        n = len(nums)
        ret = n*(n-1)//2
        for k, v in d.items():
            ret -= (v*(v-1))//2
        return ret