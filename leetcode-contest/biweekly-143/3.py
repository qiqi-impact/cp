class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        ct = Counter(nums)
        l = sorted(ct.keys())

        ls = defaultdict(int)
        
        p = [0]
        ret = 0
        for x in l:
            p.append(p[-1] + ct[x])
            ls[x-k] += ct[x]
            ls[x+k+1] -= ct[x]
        for x in l:
            left = bisect.bisect_left(l, x - k)
            right = bisect.bisect_left(l, x + k + 1)
            ret = max(ret, min(numOperations, p[right] - p[left] - ct[x]) + ct[x])
        r = sorted(ls.keys())
        cur = 0
        for x in r:
            cur += ls[x]
            ret = max(ret, min(numOperations, cur))
        return ret