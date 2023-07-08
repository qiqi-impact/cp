class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        sc = set([tuple(x) for x in coordinates])
        seen = set()
        ret = [0] * 5
        for x, y in coordinates:
            for dx in [-1, 0]:
                for dy in [-1, 0]:
                    tx, ty = x+dx, y+dy
                    if (tx, ty) not in seen and 0 <= tx < m-1 and 0 <= ty < n-1:
                        cur = 0
                        for i in [0, 1]:
                            for j in [0, 1]:
                                nx, ny = tx+i, ty+j
                                if (nx, ny) in sc:
                                    cur += 1
                        ret[cur] += 1
                        seen.add((tx, ty))
        ret[0] = (m-1) * (n-1) - sum(ret)
        return ret