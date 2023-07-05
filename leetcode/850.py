class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        ev = defaultdict(list)
        for a, b, c, d in rectangles:
            ev[a].append((b, 1))
            ev[a].append((d, -1))
            ev[c].append((b, -1))
            ev[c].append((d, 1))
        seg = {}
        prv = 0
        width = 0
        ret = 0
        for k in sorted(ev.keys()):
            ret += width * (k - prv)
            for x, d in ev[k]:
                seg[x] = seg.get(x, 0) + d
                if seg[x] == 0:
                    del seg[x]
            width = 0
            st = 0
            left = None
            for x in sorted(seg.keys()):
                st += seg[x]
                if st > 0 and left is None:
                    left = x
                if st == 0 and left is not None:
                    width += x - left
                    left = None
            prv = k
        return ret % (10**9+7)
