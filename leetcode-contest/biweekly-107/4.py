from collections import deque

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        qs = sorted(list(set(queries)))
        ans = {}
        
        ct = {}
        q = deque()
        
        l = sorted([tuple(x) for x in logs], key=lambda y:y[1])
        p = 0
        for t in qs:
            while p < len(l) and l[p][1] <= t:
                q.append(p)
                if l[p][0] not in ct:
                    ct[l[p][0]] = 0
                ct[l[p][0]] += 1
                p += 1
            while q and l[q[0]][1] < t - x:
                v = l[q.popleft()]
                ct[v[0]] -= 1
                if ct[v[0]] == 0:
                    del ct[v[0]]
            ans[t] = n - len(ct)
        return [ans[x] for x in queries]