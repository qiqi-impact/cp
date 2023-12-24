class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # print()
        g = {}
        
        for i in range(len(original)):
            a, b, c = original[i], changed[i], cost[i]
            if a not in g:
                g[a] = {}
            g[a][b] = min(g[a].get(b, inf), c)
        
        @cache
        def dfp(x):
            START = 0, x
            h = [START]
            dist = {START[1]: 0}
            while h:
                cost, cur = heapq.heappop(h)
                if dist[cur] != cost:
                    continue
                for o, w in g.get(cur, {}).items():
                    if dist.get(o, inf) > cost + w:
                        dist[o] = cost + w
                        heapq.heappush(h, (cost + w, o))
            return dist
        
        @cache
        def dp(idx):
            if idx == len(source):
                return 0
            ret = inf
            if source[idx] == target[idx]:
                ret = dp(idx+1)
            for x in original:
                if idx + len(x) <= len(source):
                    o = source[idx:idx+len(x)]
                    f = target[idx:idx+len(x)]
                    q = dfp(o)
                    if f in q:
                        ret = min(ret, q[f] + dp(idx+len(x)))
            # print(idx, ret)
            return ret
        
        v = dp(0)
        return v if v != inf else -1
                    