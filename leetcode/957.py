class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        m = [None for _ in range(1 << 8)]
        for i in range(len(m)):
            l = [0] * 8
            for j in range(8):
                if i & (1 << j):
                    l[j] = 1
            r = 0
            for j in range(1, 7):
                if not (l[j-1] ^ l[j+1]):
                    r += (1 << j)
            m[i] = r
        
        p = [m[:]]
        for _ in range(32):
            np = [None] * (1 << 8)
            for i in range(1 << 8):
                np[i] = p[-1][p[-1][i]]
            p.append(np)
        
        st = 0
        for i in range(8):
            if cells[i]:
                st ^= 1 << i
        for i in range(32):
            if n & (1 << i):
                st = p[i][st]
        ret = [0] * 8
        for i in range(8):
            ret[i] = (st >> i) & 1
        return ret