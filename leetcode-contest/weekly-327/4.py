class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        stage = [0] * k
        at0 = []
        at2 = []
        taken = False
        ev = []
        
        zz = []
        for i, (a, b, c, d) in enumerate(time):
            zz.append((i, a, b, c, d))
        zz.sort(key=lambda x:(-x[1]-x[3], -x[0]))
        
        tt = []
        for i, (_, a, b, c, d) in enumerate(zz):
            tt.append((i, a, b, c, d))
            at0.append(i)
        
        ret = 0
        ct = 0
        while 1:
            if n == 0 and len(at0) == k:
                break
            if at0 and not at2 and not taken and n >= 1:
                n -= 1
                idx = heapq.heappop(at0)
                stage[idx] = 1
                heapq.heappush(ev, (tt[idx][1] + ct, idx))
                taken = True
            elif at2 and not taken:
                idx = heapq.heappop(at2)
                stage[idx] = 3
                heapq.heappush(ev, (tt[idx][3] + ct, idx))
                taken = True
            ot = None
            while ev:
                t, idx = ev[0]
                if ot is not None and t != ot:
                    break
                ot = t
                heapq.heappop(ev)
                if stage[idx] == 1:
                    taken = False
                    stage[idx] = 2
                    heapq.heappush(ev, (tt[idx][2] + t, idx))
                elif stage[idx] == 2:
                    heapq.heappush(at2, idx)
                elif stage[idx] == 3:
                    ret = t
                    taken = False
                    stage[idx] = 0
                    heapq.heappush(ev, (tt[idx][4] + t, idx))
                elif stage[idx] == 0:
                    heapq.heappush(at0, idx)
            if ot is not None:
                ct = ot
        return ret
                