class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        ok = False
        
        n, m = len(nums), len(changeIndices)
        
        ct = defaultdict(list)
        for i, x in enumerate(changeIndices):
            ct[x-1].append(i)
        
        if len(ct) != n:
            return -1
        
        def can(x):
            l = []
            for k in ct:
                idx = bisect.bisect_left(ct[k], x)
                if idx == 0:
                    return False
                idx -= 1
                l.append((ct[k][idx], k))
            nn = nums[:]
            l.sort(reverse=True)
            pt = 0
            q = 0
            
            while nn[l[q][1]] == 0:
                q += 1
                if q == len(l):
                    return True
            
            for i in range(l[0][0], -1, -1):
                if pt < len(l) and i == l[pt][0]:
                    pt += 1
                else:
                    if q < pt:
                        nn[l[q][1]] -= 1
                    while nn[l[q][1]] == 0:
                        q += 1
                        if q == len(l):
                            return True
            return False
        
        l, r = 1, m+1
        while l < r:
            mi = (l+r)//2
            if can(mi):
                ok = True
                r = mi
            else:
                l = mi + 1
        if ok:
            return r
        return -1