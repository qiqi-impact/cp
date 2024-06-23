class Solution:
    def minimumArea(self, g: List[List[int]]) -> int:
        R, C = len(g), len(g[0])
        ar, br, ac, bc = inf, -inf, inf, -inf
        for i in range(R):
            for j in range(C):
                if g[i][j]:
                    ar = min(ar, i)
                    br = max(br, i)
                    ac = min(ac, j)
                    bc = max(bc, j)
        return (br - ar + 1) * (bc - ac + 1)