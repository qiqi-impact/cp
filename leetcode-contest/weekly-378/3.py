class Solution:
    def maximumLength(self, s: str) -> int:
        runs = defaultdict(list)
        lst = None
        l = 0
        for c in s + '.':
            if c != lst:
                if lst != None:
                    runs[lst].append(l)
                lst = c
                l = 1
            else:
                l += 1
        # print(runs)
        
        mx = -1
        for k in runs:
            l = sorted(runs[k], reverse=True)
            q = l[0]-2
            if len(l) >= 2 and l[1] >= l[0] - 1:
                q = l[0]-1
            if len(l) >= 3:
                q = max(q, l[2])
            if q > 0:
                mx = max(mx, q)
        return mx