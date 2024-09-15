import random

HMOD = 2147483647
HBASE1 = random.randrange(HMOD)

class RMQ:
    def __init__(self, n):
        self.sz = 1
        self.inf = inf
        while self.sz <= n: self.sz = self.sz << 1
        self.dat = [self.inf] * (2 * self.sz - 1)
    
    def update(self, idx, x):
        idx += self.sz - 1
        self.dat[idx] = x
        while idx > 0:
            idx = (idx - 1) >> 1
            self.dat[idx] = fn(self.dat[idx * 2 + 1], self.dat[idx * 2 + 2])
            
    def query(self, a, b):
        return self.query_help(a, b, 0, 0, self.sz)
            
    def query_help(self, a, b, k, l, r):
        if r <= a or b <= l:
            return default
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            return fn(self.query_help(a, b, 2 * k + 1, l, (l + r) >> 1),
                        self.query_help(a, b, 2 * k + 2, (l + r) >> 1, r))

fn = min
default = inf


class Hashing:
    def __init__(self, s, mod=HMOD, base1=HBASE1):
        self.mod, self.base1 = mod, base1
        self._len = _len = len(s)
        f_hash, f_pow = [0] * (_len + 1), [1] * (_len + 1)
        for i in range(_len):
            f_hash[i + 1] = (base1 * f_hash[i] + s[i]) % mod
            f_pow[i + 1] = base1 * f_pow[i] % mod
        self.f_hash, self.f_pow = f_hash, f_pow

    def hashed(self, start, stop):
        return (self.f_hash[stop] - self.f_pow[stop - start] * self.f_hash[start]) % self.mod

def asc(s):
    return [ord(c) for c in s]

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        words.sort(key=lambda t:-len(t))
        hs = [Hashing(asc(w)) for w in words]
        ht = Hashing(asc(target))
        n = len(target)
        tree = RMQ(n+1)
        tree.update(n, 0)

        def can(i, x):
            q = ht.hashed(i, i + x)
            for y, h in enumerate(hs):
                if x > len(words[y]):
                    break
                z = h.hashed(0, x)
                if z == q:
                    return True
            return False
        
        for i in range(n-1, -1, -1):
            l, r = 0, n-i
            while l < r:
                mi = (l + r + 1) // 2
                if can(i, mi):
                    l = mi
                else:
                    r = mi - 1
            if l > 0:
                v = tree.query(i+1, min(n+1, i+1+l))
                tree.update(i, v + 1)
            if i == 0:
                v = tree.query(0, 1)
                return (v if v != inf else -1)
