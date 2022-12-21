class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        s = set()
        deg = defaultdict(int)
        g = [set() for _ in range(n)]
        for x, y in edges:
            x -= 1
            y -= 1
            g[x].add(y)
            g[y].add(x)
            deg[x] += 1
            deg[y] += 1
        for k in deg:
            if deg[k] % 2:
                s.add(k)
                if len(s) > 4:
                    return False
        if len(s) == 0:
            return True
        elif len(s) == 4:
            l = list(s)
            for i in range(1, 4):
                if l[i] not in g[l[0]]:
                    ll = l[:]
                    ll.remove(l[0])
                    ll.remove(l[i])
                    if ll[0] not in g[ll[1]]:
                        return True
            return False
        else:
            l = list(s)
            if l[0] not in g[l[1]]:
                return True
            for k in range(n):
                if k not in g[l[0]] and k not in g[l[1]]:
                    return True
            return False