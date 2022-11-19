class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[float]:
        N = len(trees)
        def dp(idx, R):
            if idx == N or len(R) == 3:
                if len(R) == 0:
                    return [trees[-1][0], trees[-1][1], 0]
                elif len(R) < 3:
                    cx, cy = 0, 0
                    for b in R:
                        cx += trees[b][0]
                        cy += trees[b][1]
                    cx /= len(R)
                    cy /= len(R)
                    r = 0
                    for b in R:
                        r = max(r, (cx-trees[b][0])**2 + (cy-trees[b][1])**2)
                    return [cx, cy, r]
                else:
                    A, B, C = [trees[i] for i in R]
                    D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
                    AA = A[0]**2 + A[1]**2
                    BB = B[0]**2 + B[1]**2
                    CC = C[0]**2 + C[1]**2
                    
                    cx = (AA * (B[1] - C[1]) + BB * (C[1] - A[1]) + CC * (A[1] - B[1]))/D
                    cy = (AA * (C[0] - B[0]) + BB * (A[0] - C[0]) + CC * (B[0] - A[0]))/D
                          
                    r = 0
                    for b in R:
                        r = max(r, (cx-trees[b][0])**2 + (cy-trees[b][1])**2)
                    return [cx, cy, r]

            x, y, r = dp(idx+1, R)
            if (x-trees[idx][0]) ** 2 + (y - trees[idx][1]) ** 2 <= r:
                return [x, y, r]
            nr = tuple(list(R) + [idx])
            return dp(idx+1, nr)
        x, y, r = dp(0, tuple())
        return [x, y, math.sqrt(r)]