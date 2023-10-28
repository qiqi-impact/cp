class LST:
    def __init__(self, n):
        self.n = n
        self.t = [0] * 4*n
        self.lazy = [0] * 4*n
    
    def push(self, v):
        self.t[v*2] += self.lazy[v]
        self.lazy[v*2] += self.lazy[v]
        self.t[v*2+1] += self.lazy[v]
        self.lazy[v*2+1] += self.lazy[v]
        self.lazy[v] = 0

    def build(self, data, v, tl, tr):
        if tl == tr:
            self.t[v] = data[tl]
        else:
            tm = (tl + tr)//2
            self.build(data, v*2, tl, tm)
            self.build(data, v*2 + 1, tm + 1, tr)
            self.t[v] = 0

    def update(self, v, tl, tr, l, r, amt):
        if l > r:
            return
        if l == tl and r == tr:
            self.t[v] += amt
            self.lazy[v] += amt
        else:
            self.push(v)
            tm = (tl + tr)//2
            self.update(v*2, tl, tm, l, min(r, tm), amt)
            self.update(v*2+1, tm+1, tr, max(l, tm+1), r, amt)
            self.t[v] = max(self.t[v*2], self.t[v*2+1])

    def query(self, v, tl, tr, l, r):
        if l > r:
            return -10**9
        if l == tl and r == tr:
            return self.t[v]
        self.push(v)
        tm = (tl + tr)//2
        return max(self.query(v*2, tl, tm, l, min(r, tm)), self.query(v*2+1, tm+1, tr, max(l, tm+1), r))

lst = LST(4)
lst.build([0, 2, 0, 0], 1, 0, 3)
# lst.update(1, 0, 3, 1, 2, 1)
# lst.update(1, 0, 3, 1, 1, 2)
for i in range(4):
    print(lst.query(1, 0, 3, i, i))