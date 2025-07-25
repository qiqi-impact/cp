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
    d = defaultdict(int)
    for k in l:
        d[k] += l[k]
    for k in r:
        d[k] += r[k]
    return d

def e():
    return defaultdict(int)

class Solution:
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        @cache
        def calc2(x):
            if x == 1:
                return 0
            y = x.bit_count()
            return 1 + calc2(y)
            
        def calc(x):
            if x <= 50:
                return calc2(x)
            y = x.bit_count()
            return 1 + calc2(y)

        v = [{calc(x): 1} for x in nums]
        t = Segtree(v)
        ret = []
        for q in queries:
            if q[0] == 2:
                _, idx, val = q
                t.set(idx, {calc(val):1})
            else:
                _, l, r, k = q
                d = t.prod(l, r+1)
                ret.append(d.get(k, 0))
        return ret
                
        