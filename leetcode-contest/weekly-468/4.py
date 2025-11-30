class Node:
    def __init__(self, l, r, arr):
        self.l = l
        self.r = r
        if l == r:
            self.v = [arr[l]]
            self.left = self.right = None
            self.sm = self.mn = self.mx = arr[l]
        else:
            mi = (l + r) // 2
            self.left = Node(l, mi, arr)
            self.right = Node(mi + 1, r, arr)
            self.v = []
            self.sm = self.left.sm + self.right.sm
            ap, bp = 0, 0
            while ap < len(self.left.v) or bp < len(self.right.v):
                if ap == len(self.left.v):
                    w = 1
                elif bp == len(self.right.v):
                    w = 0
                elif self.left.v[ap] < self.right.v[bp]:
                    w = 0
                else:
                    w = 1
                if w == 0:
                    self.v.append(self.left.v[ap])
                    ap += 1
                else:
                    self.v.append(self.right.v[bp])
                    bp += 1
            self.mn = self.v[0]
            self.mx = self.v[-1]
    def get_nodes(self, l, r, ret):
        if l <= self.l and r >= self.r:
            ret.append(self)
            return
        elif self.l > r or self.r < l:
            return
        else:
            self.left.get_nodes(l, r, ret)
            self.right.get_nodes(l, r, ret)
    def cost_to(self, x):
        if self.mn >= x:
            return self.sm - (self.r - self.l + 1) * x
        if self.mx <= x:
            return (self.r - self.l + 1) * x - self.sm
        return self.left.cost_to(x) + self.right.cost_to(x)
        

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        root = Node(0, n-1, nums)
        ct = [0]
        cur = 0
        for i in range(1, n):
            if nums[i] % k != nums[i-1] % k:
                cur += 1
            ct.append(cur)
        ret = []
        for a, b in queries:
            if ct[a] != ct[b]:
                ret.append(-1)
                continue
            h = (b - a) // 2 + 1
            nodes = []
            root.get_nodes(a, b, nodes)
            L = min([node.mn for node in nodes])
            R = max([node.mx for node in nodes])
            while L < R:
                mi = (L + R) // 2
                cur = 0
                for node in nodes:
                    t = bisect.bisect_right(node.v, mi)
                    cur += t
                    if cur >= h:
                        break
                if cur >= h:
                    R = mi
                else:
                    L = mi + 1
            r = 0
            for node in nodes:
                r += node.cost_to(R) // k
            ret.append(r)
        return ret










                    
        