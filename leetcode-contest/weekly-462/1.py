class Solution:
    def reverseSubmatrix(self, g: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        t = [v[:] for v in g]
        R, C = len(g), len(g[0])
        for i in range(R):
            for j in range(C):
                if x <= i < x + k and y <= j < y + k:
                    t[i][j] = g[x+k-1-(i-x)][j]
        return t©leetcode