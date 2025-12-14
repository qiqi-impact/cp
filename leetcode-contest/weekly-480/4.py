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

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        v = [1]
        for i in range(1, len(s)):
            v.append(int(s[i] != s[i-1]))
        qq = [c for c in s]
        
        t = FenwickTree(v)
        ret = []
        for q in queries:
            if q[0] == 1:
                idx = q[1]
                if idx > 0:
                    if qq[idx] == qq[idx-1]:
                        t.set(idx, 1)
                    else:
                        t.set(idx, 0)
                if idx < len(s) - 1:
                    if qq[idx] == qq[idx+1]:
                        t.set(idx+1, 1)
                    else:
                        t.set(idx+1, 0)
                qq[idx] = 'B' if qq[idx] == 'A' else 'A'
            else:
                ss = t.query(1 + q[2]) - t.query(q[1])
                ret.append(q[2] - q[1] + 1 - ss - int(q[1] != 0 and qq[q[1]] == qq[q[1] - 1]))
        return ret