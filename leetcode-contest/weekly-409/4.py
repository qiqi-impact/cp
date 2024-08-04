from sortedcontainers import SortedList

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        sl = SortedList()
        n = len(colors)
        l = []
        for i in range(n):
            l.append(int(colors[i] != colors[(i+1)%n]))
        p = []
        cts = {}
        
        def addseg(q):
            sl.add(q)
            t = q[1] - q[0] + 1
            if t not in cts:
                cts[t] = 0
            cts[t] += 1
            
        def rmseg(q):
            sl.remove(q)
            t = q[1] - q[0] + 1
            cts[t] -= 1
            if cts[t] == 0:
                del cts[t]
        
        
        for i in range(n):
            if l[i] and not p:
                p.append(i)
            if not l[i] and p:
                p.append(i-1)
                addseg(tuple(p))
                p = []
        if p:
            p.append(n-1)
            addseg(tuple(p))
        
        def fin(v):
            if not 0 <= v < n:
                return None
            a = sl.bisect_left((v, v))
            for x in [a, a-1]:
                if 0 <= x < len(sl):
                    g, h = sl[x]
                    if g <= v <= h:
                        return (g, h)
            return None
        
        
        
        def flip(idx):
            l[idx] = 1 - l[idx]
            if l[idx] == 1:
                a = fin(idx - 1)
                c = fin(idx + 1)
                if not a and not c:
                    addseg((idx, idx))
                elif a and c:
                    rmseg(a)
                    rmseg(c)
                    addseg((a[0], c[1]))
                elif a:
                    rmseg(a)
                    addseg((a[0], idx))
                else:
                    rmseg(c)
                    addseg((idx, c[1]))
            else:
                a, b = fin(idx)
                if a == b:
                    rmseg((a, b))
                elif a < idx < b:
                    rmseg((a, b))
                    addseg((a, idx-1))
                    addseg((idx+1, b))
                elif a == idx:
                    rmseg((a, b))
                    addseg((a+1, b))
                else:
                    rmseg((a, b))
                    addseg((a, b-1))
        
        
        ret = []
        for q in queries:
            if len(q) == 3:
                _, x, y = q
                if colors[x] != y:
                    colors[x] = y
                    flip(x)
                    flip((x-1)%n)
            else:
                _, p = q
                if len(sl) == 1 and sl[0] == (0, n-1):
                    ret.append(n)
                else:
                    cur = 0
                    for t in cts:
                        if t >= p - 1:
                            v = cts[t]
                            cur += v * (t - p + 2)
                    if sl and sl[0][0] == 0 and sl[-1][1] == n-1:
                        a = sl[0][1] - sl[0][0] + 1
                        b = sl[-1][1] - sl[-1][0] + 1
                        if a + b >= p - 1:
                            cur += a + b - p + 2
                        if a >= p - 1:
                            cur -= a - p + 2
                        if b >= p - 1:
                            cur -= b - p + 2
                    ret.append(cur)
        return ret
                            
                       
                       