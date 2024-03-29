class Fenwick:
    def __init__(self, n):
        self.arr = [0] * (n+1)
    def sum(self, idx):
        idx += 1
        ret = 0
        while idx > 0:
            ret += self.arr[idx]
            idx -= idx & -idx
        return ret
    def add(self, idx, val):
        idx += 1
        while idx < len(self.arr):
            self.arr[idx] += val
            idx += idx & -idx

f = Fenwick(10)
f.add(0, 5)
f.add(4, 5)
f.add(9, 5)
for i in range(10):
    print(i, f.sum(i))