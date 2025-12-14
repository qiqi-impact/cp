class Solution:
    def minMoves(self, b: List[int]) -> int:
        if sum(b) < 0:
            return -1
        st = None
        cur = None
        for i, x in enumerate(b):
            if x < 0:
                st = i
                cur = -x
        if st is None:
            return 0
        n = len(b)
        ret = 0
        for dx in range(1, n):
            l, r = st-dx, st+dx
            l %= n
            r %= n
            if b[l] > 0:
                t = min(b[l], cur)
                b[l] -= t
                cur -= t
                ret += t * dx
            if b[r] > 0:
                t = min(b[r], cur)
                b[r] -= t
                cur -= t
                ret += t * dx
            if cur == 0:
                break
        return ret