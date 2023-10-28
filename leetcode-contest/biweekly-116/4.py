MOD = 10**9+7

class LST:
    def __init__(self, n):
        self.t = [0] * 4*n
        self.sq = [0] * 4*n
        self.lazy = [0] * 4*n
        self.build([0] * n, 1, 0, n-1)
    
    def push(self, v, tl, tr):
        if self.lazy[v]:
            tm = (tl + tr)//2
            ll = tm - tl + 1
            rl = tr - tm
            self.sq[v*2] += self.lazy[v] * self.lazy[v] * ll + 2 * self.lazy[v] * self.t[v*2]
            self.sq[v*2] %= MOD
            self.t[v*2] += self.lazy[v] * ll
            self.t[v*2] %= MOD
            self.lazy[v*2] += self.lazy[v]
            self.sq[v*2+1] += self.lazy[v] * self.lazy[v] * rl + 2 * self.lazy[v] * self.t[v*2+1]
            self.sq[v*2+1] %= MOD
            self.t[v*2+1] += self.lazy[v] * rl
            self.t[v*2+1] %= MOD
            self.lazy[v*2+1] += self.lazy[v]
            self.lazy[v] = 0

    def build(self, data, v, tl, tr):
        if tl == tr:
            self.t[v] = data[tl]
            self.sq[v] = self.t[v] * self.t[v]
            self.sq[v] %= MOD
        else:
            tm = (tl + tr)//2
            self.build(data, v*2, tl, tm)
            self.build(data, v*2 + 1, tm + 1, tr)
            self.t[v] = self.t[2*v] + self.t[2*v + 1]
            self.t[v] %= MOD
            self.sq[v] = self.sq[2*v] + self.sq[2*v + 1]
            self.sq[v] %= MOD

    def update(self, v, tl, tr, l, r, amt):
        if l > r:
            return
        if l == tl and r == tr:
            ln = tr - tl + 1
            self.sq[v] += amt * amt * ln + 2 * amt * self.t[v]
            self.sq[v] %= MOD
            self.t[v] += amt * ln
            self.t[v] %= MOD
            self.lazy[v] += amt
        else:
            self.push(v, tl, tr)
            tm = (tl + tr)//2
            self.update(v*2, tl, tm, l, min(r, tm), amt)
            self.update(v*2+1, tm+1, tr, max(l, tm+1), r, amt)
            self.t[v] = self.t[v*2] + self.t[v*2+1]
            self.t[v] %= MOD
            self.sq[v] = self.sq[v*2] + self.sq[v*2+1]
            self.sq[v] %= MOD

    def query(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.sq[v]
        self.push(v, tl, tr)
        tm = (tl + tr)//2
        return (self.query(v*2, tl, tm, l, min(r, tm)) + self.query(v*2+1, tm+1, tr, max(l, tm+1), r)) % MOD

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        prev = {}
        lst = LST(n)
        ret = 0
        for i, x in enumerate(nums):
            v = -1
            if x in prev:
                v = prev[x]
            # lst.add(v+1, i+1)
            lst.update(1, 0, n-1, v+1, i, 1)
            ret += lst.query(1, 0, n-1, 0, n-1)
            prev[x] = i
        return ret % (10**9+7)