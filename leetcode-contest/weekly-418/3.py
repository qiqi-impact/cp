class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        ct = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        for i in range(n):
            ct[len(g[i])].append(i)
        print(ct)
        if 1 in ct:
            i = ct[1][0]
            if len(g[i]) == 1:
                prv = None
                cur = i
                ret = [[i]]
                while 1:
                    f = 0
                    for x in g[cur]:
                        if x != prv:
                            ret[-1].append(x)
                            prv = cur
                            cur = x
                            f = 1
                            break
                    if not f:
                        return ret
        else:
            cur = ct[2][0]
            used = set([cur])
            d = {(0, 0): cur}
            x, y = 0, 1

            while 1:
                p = d[x,y-1]
                a = g[p]
                o = 0
                a.sort(key=lambda x:len(g[x]))
                for t in a:
                    if t not in used and len(g[t]) <= 3:
                        d[x,y] = t
                        used.add(t)
                        g[t].remove(p)
                        g[p].remove(t)
                        if len(g[t]) == 1:
                            o = 1
                        break
                if o:
                    break
                y += 1
            C = len(d)
            R = n // C
            for i in range(1, R):
                for j in range(C):
                    p = d[i-1,j]
                    l = g[p][:]
                    l.sort(key=lambda x:len(g[x]))
                    d[i,j] = l[0]
                    g[l[0]].remove(p)
                    g[p].remove(l[0])
                    if j > 0:
                        p = d[i,j-1]
                        g[l[0]].remove(p)
                        g[p].remove(l[0])
            ret = [[None for _ in range(C)] for _ in range(R)]
            for i in range(R):
                for j in range(C):
                    ret[i][j] = d[i,j]
            return ret
