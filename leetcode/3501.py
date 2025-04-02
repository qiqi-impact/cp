def bit_ceil(n):
    x = 1
    while x < n: x *= 2
    return x

def countr_zero(n):
    for i in range(32):
        if n & 1 << i:
            return i
    return 32

class Segtree:
    def __init__(self, v):
        n = len(v)
        self._n = n
        self.size = bit_ceil(n)
        self.log = countr_zero(self.size)
        self.d = [e() for _ in range(2 * self.size)]
        for i in range(n):
            self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def _psh(self, p):
        for i in range(self.log, 0, -1):
            self.push(p >> i)

    def _upd(self, p):
        for i in range(1, self.log + 1):
            self.update(p >> i)

    def set(self, p, x):
        assert 0 <= p and p < self._n
        p += self.size
        self.d[p] = x
        self._upd(p)

    def get(self, p):
        assert 0 <= p and p < self._n
        return self.d[p + self.size]

    def prod(self, l, r):
        # assert 0 <= l and l <= r and r <= self._n
        l = max(l, 0)
        r = min(r, self._n)
        
        if l >= r: return e()
        l += self.size
        r += self.size
        sml, smr = e(), e()
        while l < r:
            if l & 1:
                sml = op(sml, self.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = op(self.d[r], smr)
            l >>= 1
            r >>= 1

        return op(sml, smr)
    
    def all_prod(self):
        return self.d[1]

    # maximum i s.t. g(a[l]...a[i]) == True
    def max_right(self, l, g):
        assert 0 <= l and l <= self._n
        assert g(e())
        if l == self._n: return self._n
        l += self.size
        sm = e()
        while True:
            while l % 2 == 0: l >>= 1
            if not g(op(sm, self.d[l])):
                while l < self.size:
                    l = 2 * l
                    if g(op(sm, self.d[l])):
                        sm = op(sm, self.d[l])
                        l += 1
                return l - self.size
            sm = op(sm, self.d[l])
            l += 1
            if l & -l == l:
                break
        return self._n

    # minimum i s.t. g(a[i]...a[r - 1]) == True
    def min_left(self, r, g):
        assert 0 <= r and r <= self._n
        assert g(e())
        if r == 0: return 0
        r += self.size
        sm = e()
        while True:
            r -= 1
            while r > 1 and r % 2: r >>= 1
            if not g(op(self.d[r], sm)):
                while r < self.size:
                    r = 2 * r + 1
                    if g(op(self.d[r], sm)):
                        sm = op(self.d[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = op(self.d[r], sm)
            if r & -r == r:
                break
        return 0

    def update(self, k):
        self.d[k] = op(self.d[2 * k], self.d[2 * k + 1])

def op(l, r):
    return max(l, r)

def e():
    return -inf

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        l = []
        cur = None
        s = [int(x) for x in s] + [1]
        n = len(s)
        for i in range(n):
            if s[i] == 0:
                if cur is None:
                    cur = [i]
            else:
                if cur:
                    l.append(cur + [i-1])
                    cur = None
        v = [x[1] - x[0] + 1 for x in l]
        adj = []
        for i in range(len(v)-1):
            adj.append(v[i] + v[i+1])
        t = Segtree(adj)
        
        ret = []
        for a, b in queries:
            mx = 0
            ai = bisect.bisect_left(l, [a, a])

            if ai != len(l) and l[ai][0] == a:
                pass
            elif ai != 0 and l[ai-1][1] >= a:
                ai -= 1

            bi = bisect.bisect_left(l, [b, b])
            if bi != len(l) and l[bi][0] == b:
                pass
            elif bi != 0 and l[bi-1][1] >= b:
                bi -= 1

            if ai == len(l):
                ret.append(0)
                continue

            if ai == bi:
                ret.append(0)
                continue

            cz = l[ai][1] - max(l[ai][0], a) + 1
            if ai == len(l) - 1 or l[ai+1][0] > b:
                ret.append(0)
                continue
            elif l[ai+1][0] <= b <= l[ai+1][1]:
                mx = max(mx, cz + b - l[ai+1][0] + 1)
            else:
                mx = max(mx, cz + l[ai+1][1] - l[ai+1][0] + 1)

            if bi < len(l) and l[bi][0] <= b <= l[bi][1]:
                cz = b - l[bi][0] + 1
                if bi == 0:
                    ret.append(0)
                    continue
                elif l[bi-1][0] <= a <= l[bi-1][1]:
                    pass
                else:
                    mx = max(mx, cz + l[bi-1][1] - l[bi-1][0] + 1)

            L, R = ai+1, bi-2
            if L <= R:
                mx = max(mx, t.prod(L, R+1))

            ret.append(mx)
        q = sum(s) - 1
        return [q + x for x in ret]