def normalize(arr):
    ll = sorted(set(arr))
    m = {ll[i]:i for i in range(len(ll))}
    return [m[x] for x in arr]

def dn(c):
    a, b = [x[0] for x in c], [x[1] for x in c]
    a = normalize(a)
    b = normalize(b)
    return [(a[i], b[i]) for i in range(len(c))]

class Solution:
    def maxPathLength(self, c: List[List[int]], k: int) -> int:
        c = dn(c)
        tx, ty = c[k]
        a, b = [], []
        for x, y in c:
            if (x < tx and y < ty):
                a.append((x, y))
            if (x > tx and y > ty):
                b.append((x, y))
        a = dn(a)
        b = dn(b)

        def lis2(arr):
            arr.sort(key=lambda x:(x[0], -x[1]))
            dp = [0] * len(arr)
            mx = 0
            tree = Segtree(dp)
            for x, y in arr:
                v = tree.prod(0, y)
                tree.set(y, v+1)
                mx = max(mx, v+1)
            return mx
    
        return lis2(a) + lis2(b) + 1