class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        g1 = defaultdict(dict)
        g2 = defaultdict(dict)

        p = set()
        
        for i in range(len(rates1)):
            x, y = pairs1[i]
            g1[x][y] = rates1[i]
            g1[y][x] = 1. / rates1[i]
            p.add(x)
            p.add(y)
        for i in range(len(rates2)):
            x, y = pairs2[i]
            g2[x][y] = rates2[i]
            g2[y][x] = 1. / rates2[i]
            p.add(x)
            p.add(y)

        d = {initialCurrency: 1.}
        q = deque([initialCurrency])
        while q:
            x = q.popleft()
            for ch in g1[x]:
                if ch not in d:
                    d[ch] = g1[x][ch] * d[x]
                    q.append(ch)

        e = {initialCurrency: 1.}
        q = deque([initialCurrency])
        while q:
            x = q.popleft()
            for ch in g2[x]:
                if ch not in e:
                    e[ch] = g2[x][ch] * e[x]
                    q.append(ch)

        ret = 1.
        for k in d:
            if k in e:
                ret = max(ret, d[k] / e[k])
        return ret

    