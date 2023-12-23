class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d = {
            'N': [-1, 0],
            'S': [1, 0],
            'E': [0, 1],
            'W': [0, -1],
        }
        cx, cy = 0, 0
        s = set([(0, 0)])
        for c in path:
            cx += d[c][0]
            cy += d[c][1]
            if (cx, cy) in s:
                return True
            s.add((cx, cy))
        return False