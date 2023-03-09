class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        h = []
        ret = 0
        cur = 0
        for x, y in stations + [[target, 0]]:
            startFuel -= x - cur
            while startFuel < 0:
                if not h:
                    return -1
                z = heapq.heappop(h)
                startFuel -= z
                ret += 1
            heapq.heappush(h, -y)
            cur = x
        return ret