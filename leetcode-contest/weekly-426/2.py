class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        sm = sum(nums)
        mx = -inf
        for i, x in enumerate(nums):
            cur = sm - x
            if cur % 2:
                continue
            c = cur // 2
            if c not in d:
                continue
            l = d[c]
            if len(l) >= 2 or l[0] != i:
                mx = max(mx, x)
        return mx