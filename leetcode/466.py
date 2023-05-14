class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        a, b = Counter(s1), Counter(s2)
        for k in b:
            if b[k] * n2 > a[k] * n1:
                return 0

        l1, l2 = len(s1), len(s2)
        dp = [[None for _ in range(l1)] for _ in range(32)]

        for st in range(l1):
            steps = 0
            pt2 = 0
            pt1 = st
            while 1:
                steps += 1
                if s1[pt1] == s2[pt2]:
                    pt2 += 1
                    if pt2 == l2:
                        dp[0][st] = steps
                        break
                pt1 += 1
                pt1 %= l1

        for pw in range(1, 32):
            for st in range(l1):
                p = dp[pw-1][st]
                dp[pw][st] = p + dp[pw-1][(st+p)%l1]

        def can(x):
            rq = x * n2
            cur = 0
            steps = 0
            for i in range(31, -1, -1):
                if rq & (1 << i):
                    v = dp[i][cur]
                    cur = (cur + v)%l1
                    steps += v
                    if steps > l1 * n1:
                        return False
            return True

        l, r = 1, 10**8
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l