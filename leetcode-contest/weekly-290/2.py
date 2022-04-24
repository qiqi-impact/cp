class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ret = 0
        seen = [[0 for _ in range(201)] for _ in range(201)]
        for (x, y, r) in circles:
            for i in range(x-r, x+r+1):
                for j in range(y-r, y+r+1):
                    if not seen[i][j]:
                        if (x-i)**2 + (y-j)**2 <= r**2:
                            seen[i][j] = 1
                            ret += 1
        return ret