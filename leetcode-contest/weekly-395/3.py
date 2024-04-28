class Solution:
    def minEnd(self, n: int, x: int) -> int:
        b = bin(n-1)
        bp = len(b)-1
        # print(b)
        ret = 0
        for t in range(64):
            if (x & (1 << t)) == 0:
                if b[bp] != 'b':
                    ret ^= (int(b[bp]) << t)
                    bp -= 1
            else:
                ret ^= (1 << t)
        return ret