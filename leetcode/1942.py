class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        occ = {}
        
        ev = []
        for i, (x, y) in enumerate(times):
            ev.append((x, True, i))
            ev.append((y, False, i))
        ev.sort()
        
        h = list(range(n))
        for t, o, idx in ev:
            if o:
                q = heapq.heappop(h)
                if idx == targetFriend:
                    return q
                occ[idx] = q
            else:
                q = occ[idx]
                del occ[idx]
                heapq.heappush(h, q)