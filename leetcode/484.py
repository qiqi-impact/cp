class Solution:
    def findPermutation(self, s: str) -> List[int]:
        s += 'I'
        n = len(s)
        l = list(range(1, n+1))
        drun = 0
        for i in range(n):
            if s[i] == 'D':
                drun += 1
            else:
                if drun > 0:
                    sm = 2*(i+1) - drun
                    for j in range(i-drun, i+1):
                        l[j] = sm - l[j]
                drun = 0
        return l