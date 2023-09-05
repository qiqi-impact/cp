class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        mnx, mxx, mny, mxy = inf, -inf, inf, -inf
        ls = {}
        for a, b, c, d in rectangles:
            mnx = min(mnx, a)
            mny = min(mny, b)
            mxx = max(mxx, c)
            mxy = max(mxy, d)
            for x, y, z in [[a, b, 1], [c, b, -1], [a, d, -1], [c, d, 1]]:
                if x not in ls:
                    ls[x] = {}
                if y not in ls[x]:
                    ls[x][y] = 0
                ls[x][y] += z
        cur = {}
        ks = sorted(ls.keys())
        for i, x in enumerate(ks):
            for y in ls[x]:
                cur[y] = cur.get(y, 0) + ls[x][y]
                if cur[y] == 0:
                    del cur[y]
            if i == len(ks)-1:
                if len(cur) != 0:
                    return False
            else:
                if len(cur) != 2 or cur.get(mny, 0) != 1 or cur.get(mxy, 0) != -1:
                    return False
        return True