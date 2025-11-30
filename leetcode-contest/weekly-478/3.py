class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        @cache
        def mirror(x):
            return int(str(x)[::-1])
        ind = defaultdict(list)
        for i, x in enumerate(nums):
            ind[x].append(i)
        ret = inf
        for i, x in enumerate(nums):
            mx = mirror(x)
            if mx in ind:
                t = bisect.bisect_left(ind[mx], i + 1)
                if t <= len(ind[mx]) - 1:
                    ret = min(ret, ind[mx][t] - i)
        return ret if ret != inf else -1