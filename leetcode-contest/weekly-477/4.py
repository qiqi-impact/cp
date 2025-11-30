class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        runs = []
        lst = inf
        n = len(nums)
        for i, x in enumerate(nums):
            if x < lst:
                runs.append(i)
            lst = x
        runs.append(n)
        lr = len(runs)

        tot = [0]
        for i in range(lr - 1):
            a = runs[i]
            b = runs[i + 1]
            tot.append(tot[-1] + (b-a) * (b-a+1) // 2)

        l = []
        for a, b in queries:
            ai = bisect.bisect_right(runs, a) - 1
            bi = bisect.bisect_right(runs, b) - 1
            if ai == bi:
                l.append((b-a+1) * (b-a+2) // 2)
                continue
            cur = (runs[ai + 1] - a) * (runs[ai + 1] + 1 - a) // 2
            cur += (b - runs[bi] + 1) * (b - runs[bi] + 2) // 2
            cur += tot[bi] - tot[ai + 1]
            l.append(cur)
        return l