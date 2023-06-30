class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        h = []
        dead = set()

        ev = []
        for i, (x, y, _) in enumerate(buildings):
            ev.append((x, i, True))
            ev.append((y, i, False))
        ev.sort()
        p = 0

        ret = []
        while p < len(ev):
            t = ev[p][0]
            while p < len(ev) and ev[p][0] == t:
                x, i, b = ev[p]
                if b:
                    heapq.heappush(h, (-buildings[i][2], i))
                else:
                    dead.add(i)
                p += 1
            while h and h[0][1] in dead:
                heapq.heappop(h)
            nh = buildings[h[0][1]][2] if h else 0
            if not ret or (ret[-1][1] != nh):
                ret.append((t, nh))
        return ret