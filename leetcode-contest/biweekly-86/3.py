class Solution:
    def maximumRows(self, m: List[List[int]], cols: int) -> int:
        R, C = len(m), len(m[0])
        
        b = []
        for i in range(R):
            x = 0
            for j in range(C):
                if m[i][j]:
                    x ^= (1 << j)
            b.append(x)
        
        ret = 0
        def test(idx, oe, rows):
            nonlocal ret
            if idx == R:
                if bin(oe).count('1') <= cols:
                    ret = max(ret, rows)
                return
            test(idx+1, oe | b[idx], rows + 1)
            test(idx+1, oe, rows)
        test(0, 0, 0)
        return ret