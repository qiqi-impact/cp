class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        d = defaultdict(list)
        for x, y in points:
            d[x].append(y)
        ks = sorted(d.keys())
        for k in ks:
            d[k].sort(reverse=True)
        ret = 0
        for i, x in enumerate(ks):
            for j, y in enumerate(d[x]):
                mx = -inf
                if j != len(d[x])-1:
                    ret += 1
                    mx = d[x][j+1]
                for k in range(i+1, len(ks)):
                    xx = ks[k]
                    if d[xx]:
                        for l, yy in enumerate(d[xx]):
                            if yy > y:
                                continue
                            if yy > mx:
                                mx = yy
                                ret += 1
                            break
        return ret
