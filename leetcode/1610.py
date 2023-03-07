class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angle = angle * pi/180
        pts = [(x - location[0], y - location[1]) for x, y in points]
        
        fixed = 0
        tans = []
        for x, y in pts:
            if x == 0 and y == 0:
                fixed += 1
            else:
                tans.append(atan2(y, x))
        
        tans.sort()
        tans = tans + [x+2*math.pi for x in tans]
        j = 0
        ret = 0
        for i in range(len(tans)):
            while j < len(tans)-1 and tans[j+1] - tans[i] <= angle:
                j += 1
            ret = max(ret, j - i + 1)
        return ret + fixed