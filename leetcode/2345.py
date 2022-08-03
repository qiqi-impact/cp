class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        peaks.sort(key=lambda x:(x[0]-x[1], -(x[0]+x[1])))
        mx = float('-inf')
        ret = 0
        for i in range(len(peaks)):
            x, y = peaks[i]
            if x+y > mx:
                if i < len(peaks)-1 and (x,y) == tuple(peaks[i+1]):
                    ret -= 1
                ret += 1
            mx = max(mx, x+y)
        return ret