class Solution:
    def minimumCost(self, s: str) -> int:
        s = [int(x) for x in s]
        n = len(s)
        l0 = [0] * n
        l1 = [0] * n
        r0 = [0] * n
        r1 = [0] * n
        for i in range(n):
            if i == 0:
                l0[i] = int(s[i] != 0)
                l1[i] = int(s[i] != 1)
            else:
                if s[i] == 1:
                    l0[i] = (i+1) + l1[i-1]
                    l1[i] = l1[i-1]
                else:
                    l0[i] = l0[i-1]
                    l1[i] = (i+1) + l0[i-1]
        for i in range(n-1, -1, -1):
            if i == n-1:
                r0[i] = int(s[i] != 0)
                r1[i] = int(s[i] != 1)
            else:
                if s[i] == 1:
                    r0[i] = (n-i) + r1[i+1]
                    r1[i] = r1[i+1]
                else:
                    r0[i] = r0[i+1]
                    r1[i] = (n-i) + r0[i+1]
        ret = min(l0[n-1], l1[n-1], r0[0], r1[0])
        for i in range(n-1):
            ret = min(ret, l0[i] + r0[i+1], l1[i] + r1[i+1])
        return ret