class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        def make_dict(arr):
            d = {0: 0}
            for x in arr:
                nd = d.copy()
                for k in d:
                    a, b = d[k], d[k] - k
                    a += x
                    df = abs(a - b)
                    if df not in nd:
                        nd[df] = 0
                    nd[df] = max(nd[df], max(a, b))
                    a -= x
                    b += x
                    df = abs(a - b)
                    if df not in nd:
                        nd[df] = 0
                    nd[df] = max(nd[df], max(a, b))
                d = nd
            return d
        l, r = make_dict(rods[:len(rods)//2]), make_dict(rods[len(rods)//2:])
        ret = 0
        for k in l:
            if k in r:
                ret = max(ret, l[k] + r[k] - k)
        return ret