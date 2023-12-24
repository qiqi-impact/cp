class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = 26
        source = [ord(c)-97 for c in source]
        target = [ord(c)-97 for c in target]
        
        g = [{} for _ in range(n)]
        
        for i in range(len(original)):
            a, b, c = original[i], changed[i], cost[i]
            a = ord(a)-97
            b = ord(b)-97
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
                for o, w in g[cur].items():
                    if dist.get(o, inf) > cost + w:
                        dist[o] = cost + w
                        heapq.heappush(h, (cost + w, o))
            return dist
        
        ret = 0
        for i in range(len(source)):
            # print(source[i], target[i])
            q = dfp(source[i])
            if target[i] not in q:
                return -1
            ret += q[target[i]]
        return ret