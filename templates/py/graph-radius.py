def radius(n, edges):
    g = [set() for _ in range(n)]
    q = []
    for x, y in edges:
        g[x].add(y)
        g[y].add(x)
    for i in range(n):
        if len(g[i]) == 1:
            q.append(i)
    ret = 0
    for i in range(n):
        nq = []
        did = False
        for t in q:
            if len(g[t]) == 1:
                for k in g[t]:
                    g[k].discard(t)
                    did = True
                    if len(g[k]) == 1:
                        nq.append(k)
        if did:
            ret += 1
        if not nq:
            return ret
        q = nq
    return ret