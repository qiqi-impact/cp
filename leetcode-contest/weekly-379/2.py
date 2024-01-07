class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            cx, cy = a, b
            while 1 <= cx <= 8 and 1 <= cy <= 8 and (cx, cy) != (c, d):
                if (cx, cy) == (e, f):
                    return 1
                cx += dx
                cy += dy
        
        for dx in [-1, 1]:
            for dy in [-1, 1]:
                cx, cy = c, d
                while 1 <= cx <= 8 and 1 <= cy <= 8 and (cx, cy) != (a, b):
                    if (cx, cy) == (e, f):
                        return 1
                    cx += dx
                    cy += dy
        return 2