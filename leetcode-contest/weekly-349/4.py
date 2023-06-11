class Node:
    def __init__(self, nums, l, r):
        self.mn = nums[l]
        self.mx = nums[r]
        self.l = l
        self.r = r
        self.left = self.right = None
        if l == r:
            self.sm = 0
        else:
            mi = (l+r)//2
            self.left = Node(nums, l, mi)
            self.right = Node(nums, mi+1, r)
            self.sm = 0
    def tick(self, idx, v):
        self.sm = max(self.sm, v)
        if self.l != self.r:
            if idx <= (self.l+self.r)//2:
                self.left.tick(idx, v)
            else:
                self.right.tick(idx, v)
    def query(self, v):
        # print(self.mn, self.mx, v, 'foo', self.sm)
        if self.mx < v:
            return 0
        if self.mn >= v:
            return self.sm
        if self.l != self.r:
            return max(self.left.query(v), self.right.query(v))
        
        

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        tot = 0
        qq = sorted(queries, key=lambda x:-x[0])
        
        
        n1 = [(x, i) for (i, x) in enumerate(nums1)]
        n1.sort(reverse=True)
        p = 0
        
        inv = {}
        n2 = [(x, i) for (i, x) in enumerate(nums2)]
        n2.sort()
        for i in range(len(n2)):
            inv[n2[i][1]] = i
        q2 = sorted(nums2)
        
        root = Node(q2, 0, len(q2)-1)
        
        # print(n1, n2, queries, inv)
        ans = {}
        for x, y in qq:
            # print(x,y)
            while p != len(n1) and x <= n1[p][0]:
                t = inv[n1[p][1]]
                # print(x, t, q2[t] + n1[p][0])
                root.tick(t, q2[t] + n1[p][0])
                p += 1
            cv = root.query(y)
            # print(x,y,cv)
            if cv > 0:
                ans[x,y] = cv
        
        ret = [ans.get((x,y), -1) for (x,y) in queries]
        return ret
                
            