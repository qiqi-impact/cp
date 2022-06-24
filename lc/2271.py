class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        c = [0]
        starts = []
        ends = []
        mx = 0
        for x, y in tiles:
            starts.append(x)
            ends.append(y)
            c.append(c[-1] + (y-x+1))
        for i in range(len(tiles)):
            endval = tiles[i][0] + carpetLen - 1
            idx = bisect.bisect_right(starts, endval) - 1
            covered = c[idx+1] - c[i] - max(0, ends[idx] - endval)
            mx = max(mx, covered)
        return mx