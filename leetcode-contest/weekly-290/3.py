class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        xs = {}
        
        xset = set()
        for [x, _] in rectangles:
            xset.add(x)
        xl = sorted(list(xset))
        
        nr = [[0 for _ in range(101)] for _ in range(len(xl)+1)]
        
        for [x, y] in rectangles:
            nx = bisect.bisect_left(xl, x)
            nr[nx][y] = 1
            
        for i in range(len(xl)-1, -1, -1):
            for j in range(100, -1, -1):
                nr[i][j] += nr[i+1][j]
                if j < 100:
                    nr[i][j] += nr[i][j+1] - nr[i+1][j+1]
        
        ret = []
        for [x, y] in points:
            nx = bisect.bisect_left(xl, x)
            ret.append(nr[nx][y])
        return ret