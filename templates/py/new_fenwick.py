class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def set(self, idx, x):
        old = self.get(idx)
        self.update(idx, x - old)

    def get(self, idx):
        return self.query(idx+1) - self.query(idx)

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def query_range(self, start, end):
        """calc sum(bit[start:end])"""
        if end < start:
            return 0
        return self.query(end) - self.query(start)

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
t = FenwickTree(l)
for i in range(7):
    print(i, t.query(i))
print(t.findkth(13))