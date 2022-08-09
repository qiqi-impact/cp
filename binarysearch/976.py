class Solution:
    def solve(self, orders):
        bh = []
        sh = []
        ret = 0
        for x, y, z in orders:
            if z == 0:
                heappush(bh, [-x, y])
            else:
                heappush(sh, [x, y])
            while bh and sh and -bh[0][0] >= sh[0][0]:
                q = min(bh[0][1], sh[0][1])
                ret += q
                bh[0][1] -= q
                sh[0][1] -= q
                while bh and bh[0][1] == 0:
                    heappop(bh)
                while sh and sh[0][1] == 0:
                    heappop(sh)
        return ret