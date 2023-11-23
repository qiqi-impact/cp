class FenwickTree:
    def __init__(self, n):
        self.bit = [0] * n

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1

l = [1,3,4,2,4,10]
t = FenwickTree(6)
for i, x in enumerate(l):
    t.update(i, x)
for i in range(7):
    print(i, t.query(i))
print(t.findkth(13))