class Solution:
    def solve(self, m):
        if not m: return 0
        R, C = map(len, [m, m[0]])

        def conv(row):
            minus = [row[i] - i for i in range(C)]
            plus = [row[i] + i for i in range(C)]
            for i in range(1, C):
                plus[i] = max(plus[i], plus[i-1])
            for i in range(C-2, -1, -1):
                minus[i] = max(minus[i], minus[i+1])
            return [max(minus[i] + i, plus[i] - i) for i in range(C)]

        cur = m[0]
        for i in range(1, R):
            cc = conv(cur)
            cur = [a+b for (a, b) in zip(cc, m[i])]

        return max(cur)