class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ln = len(nums[0])
        l = [int(x) for x in nums]
        m = [None] * (ln+1)
        p = 1
        for i in range(1, ln+1):
            p *= 10
            m[i] = sorted([(x%p, i) for (i, x) in enumerate(l)])
        return [m[a][b-1][1] for (b, a) in queries]