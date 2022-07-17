class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        ret = -1
        for n in nums:
            s = str(n)
            sm = 0
            for c in s:
                sm += int(c)
            d[sm].append(n)
            d[sm].sort(reverse=True)
            if len(d[sm]) > 2:
                d[sm].pop()
            if len(d[sm]) == 2:
                ret = max(ret, sum(d[sm]))
        return ret