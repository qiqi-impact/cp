class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        ev = []
        for x, y, z in segments:
            ev.append((x, 1, z))
            ev.append((y, 0, z))
        ev.sort()
        cur = set()
        sm = 0
        start = None
        ep = 0
        ret = []
        while ep < len(ev):
            t, o, c = ev[ep]
            
            if start is not None and start != t and sm:
                ret.append([start, t, sm])
            
            if o == 1:
                cur.add(c)
                sm += c
            else:
                cur.discard(c)
                sm -= c
            ep += 1
            
            start = t
        return ret