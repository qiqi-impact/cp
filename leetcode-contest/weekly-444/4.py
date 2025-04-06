from sortedcontainers import SortedList

class Node:
    def __init__(self, v, idx):
        self.n = self.p = None
        self.v = v
        self.sm = None
        self.df = None
        self.idx = idx
    def delete(self):
        a, b = self.p, self.n
        if a:
            a.n = b
        if b:
            b.p = a
    def __repr__(self):
        return str((self.v, self.sm, self.df, self.idx))

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        l = []
        sl = SortedList()
        mp = {}
        ct = 0
        ops = 0
        for i, x in enumerate(nums):
            v = Node(x, i)
            l.append(v)
            if len(l) > 1:
                v.p = l[-2]
                l[-2].n = v
                l[-2].sm = x + l[-2].v
                l[-2].df = l[-2].v - x
                if l[-2].df > 0:
                    ct += 1
                sl.add((l[-2].sm, l[-2].idx, l[-2]))
        l[-1].delete()
        while ct > 0:
            # print(sl)
            # print(ct)
            ops += 1
            a, _, b = sl.pop(0)
            add = a - b.v
            # print(add)
            if b.df > 0:
                ct -= 1
            c, d = b.p, b.n
            if c:
                # print(c)
                sl.discard((c.sm, c.idx, c))
                c.sm += add
                if c.df > 0:
                    ct -= 1
                c.df -= add
                if c.df > 0:
                    ct += 1
                sl.add((c.sm, c.idx, c))
            if d:
                sl.discard((d.sm, d.idx, d))
                d.v += b.v
                d.sm += b.v
                if d.df > 0:
                    ct -= 1
                d.df += b.v
                if d.df > 0:
                    ct += 1
                sl.add((d.sm, d.idx, d))
            b.delete()
        return ops
            




                
                