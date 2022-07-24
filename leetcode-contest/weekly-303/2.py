class Solution:
    def equalPairs(self, g: List[List[int]]) -> int:
        r, c = len(g), len(g[0])
        
        rr = defaultdict(int)
        cc = defaultdict(int)
        
        for i in range(r):
            rr[tuple(g[i])] += 1
            
        for j in range(c):
            x = []
            for i in range(r):
                x.append(g[i][j])
            cc[tuple(x)] += 1
            
        ret = 0
        for k in rr:
            ret += rr[k] * cc[k]
        return ret