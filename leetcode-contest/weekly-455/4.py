class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        if k == 1:
            if n != 1:
                return -1
            return time[0] * mul[0]

        FULL = (1 << n) - 1

        dist = {(FULL, 0, 0): 0.}
        h = [(0., FULL, 0, 0)]
        while h:
            p = heapq.heappop(h)
            cost, bm, boat, stage = p
            if bm == 0:
                return cost
            if dist[bm, boat, stage] != cost:
                continue
            ret = inf
            if boat == 1:
                for j in range(n):
                    if not bm & 1 << j:
                        dt = time[j] * mul[stage]
                        nstage = (stage + int(dt)) % m
                        if dist.get((bm ^ (1 << j), 0, nstage), inf) > dt + cost:
                            np = (dt + cost, bm ^ (1 << j), 0, nstage)
                            heapq.heappush(h, np)
                            dist[(bm ^ (1 << j), 0, nstage)] = dt + cost
            else:
                cur = bm
                ct = bm.bit_count()
                while cur:
                    mx = 0
                    c = 0
                    for j in range(n):
                        if cur & 1 << j:
                            mx = max(mx, time[j])
                            c += 1
                    if c <= k:
                        dt = mx * mul[stage]
                        nstage = (stage + int(dt)) % m
                        if dist.get((bm ^ cur, 1, nstage), inf) > dt + cost:
                            np = (dt + cost, bm ^ cur, 1, nstage)
                            heapq.heappush(h, np)
                            dist[(bm ^ cur, 1, nstage)] = dt + cost
                    cur = (cur - 1) & bm
        return -1