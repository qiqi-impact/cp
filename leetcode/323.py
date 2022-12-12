class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cc = [i for i in range(n)]
        
        def find(x):
            if cc[x] != x:
                cc[x] = find(cc[x])
            return cc[x]
        
        def union(a, b):
            fa = find(a)
            fb = find(b)
            if fa != fb:
                cc[fb] = fa
                return 1
            return 0
        
        ret = n
        for x, y in edges:
            ret -= union(x, y)
            
        return ret