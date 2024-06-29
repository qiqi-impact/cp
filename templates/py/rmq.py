class RMQ:
    def __init__(self, n):
        self.sz = 1
        self.inf = (1 << 31) - 1
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