class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        R = len(grid)
        C = len(grid[0])
        cc = {}
        all_coords = set()
        joined = 0
        def root(i):
            if cc[i] != i:
                cc[i] = root(cc[i])
            return cc[i]
        def join(i, j):
            ri = root(i)
            rj = root(j)
            if ri != rj:
                cc[ri] = rj
            return int(ri != rj)
        for i in range(R):
            for j in range(C):
                cx, cy = 2*i+1, 2*j+1
                opts = []
                for dx,dy in D:
                    opts.append((cx+dx, cy+dy))
                    if (cx+dx, cy+dy) not in cc:
                        cc[(cx+dx, cy+dy)] = (cx+dx, cy+dy)
                    all_coords.add((cx+dx, cy+dy))
                if grid[i][j] == '/':
                    joined += join(opts[0], opts[2])
                    joined += join(opts[1], opts[3])
                elif grid[i][j] == '\\':
                    joined += join(opts[0], opts[3])
                    joined += join(opts[1], opts[2])
                else:
                    joined += join(opts[0], opts[1])
                    joined += join(opts[0], opts[2])
                    joined += join(opts[0], opts[3])
        print(len(all_coords), joined)
        return len(all_coords) - joined