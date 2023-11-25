class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        h.sort()
        v.sort()
        hr = 1
        c = 1
        for i in range(len(h)-1):
            if h[i+1] - h[i] != 1:
                c = 1
            else:
                c += 1
            hr = max(hr, c)
            
        vr = 1
        c = 1
        for i in range(len(v)-1):
            if v[i+1] - v[i] != 1:
                c = 1
            else:
                c += 1
            vr = max(vr, c)
            
        t = min(vr, hr)
        return (t+1) * (t+1)