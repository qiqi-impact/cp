from functools import cache


SIGNATURE = [int, int, int, str]


class Solution:
    def F(self, start: int, finish: int, limit: int, s: str) -> int:
        for c in s:
            if int(c) > limit:
                return 0
            
        finish = [int(c) for c in str(finish)]
        start = [int(c) for c in str(start-1)]
        if len(start) < len(finish):
            start = ([0]*(len(finish)-len(start))) + start
        s = [int(c) for c in s]
        
        q = [start, finish]
        
        @cache
        def dp(li, idx, cap):
            L = q[li]
            if idx == len(q[li]):
                # print(li, idx, cap, 1, p)
                return 1
            ret = 0
            mx = limit
            if cap:
                mx = min(mx, L[idx])
            for dig in range(mx+1):
                if idx >= len(L)-len(s):
                    if dig != s[idx - (len(L)-len(s))]:
                        continue
                iscap = cap and dig == L[idx]
                ret += dp(li, idx+1, iscap)
            # print(li, idx, cap, ret, p)
            return ret
        
        return dp(1, 0, True) - dp(0, 0, True)







with open("test_contest_in") as f:
    tc = []
    for i, l in enumerate(f.read().splitlines()):
        if l[0] == '"' and l[-1] == '"':
            l = l[1:-1]
        l = SIGNATURE[i%len(SIGNATURE)](l)
        tc.append(l)
        if len(tc) == len(SIGNATURE):
            print(Solution().F(*tc))
            tc = []