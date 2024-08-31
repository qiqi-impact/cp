class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        s = [int(x) for x in s]
        l = []
        pf = [0]
        n = len(s)
        j = 0
        ct = [0, 0]
        for i in range(n):
            while j < n and (ct[0] + (s[j] == 0) <= k or ct[1] + (s[j] == 1) <= k):
                ct[s[j]] += 1
                j += 1
            l.append(j - 1)
            pf.append(pf[-1] + l[-1])
            ct[s[i]] -= 1
        
        pt = n
        
        ans = {}
        qs = sorted(queries, key=lambda x:-x[1])
        for x, y in qs:
            while pt != 0 and l[pt-1] >= y:
                pt -= 1
            sub = -((x - 2) * (y - x + 1) + (y - x + 1) * (y - x + 2) // 2)
            if pt <= x:
                sub += y * (y - x + 1)
            elif pt > y:
                sub += pf[y+1] - pf[x]
            else:
                sub += pf[pt] - pf[x] + (y - pt + 1) * y
            ans[x, y] = sub
        ret = []
        for x, y in queries:
            ret.append(ans[x, y])
        return ret
        
        
        
        