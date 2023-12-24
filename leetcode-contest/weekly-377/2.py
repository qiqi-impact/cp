class Solution:
    def maximizeSquareArea(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        h = [1, m] + h
        v = [1, n] + v
        h.sort()
        v.sort()
        
        ret = -1
        
        s = set()
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                s.add(v[j] - v[i])
        
        
        for i in range(len(h)):
            for j in range(i+1, len(h)):
                dx = h[j] - h[i]
                if dx in s:
                    ret = max(ret, dx)
                    
        return (ret * ret) % (10**9+7) if ret != -1 else -1