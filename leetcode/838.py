class Solution:
    def pushDominoes(self, d: str) -> str:
        n = len(d)
        l = [0] * n
        INF = float('inf')
        cur = INF
        ans = []
        
        for i in range(n-1, -1, -1):
            if d[i] == 'L':
                cur = -1
            elif d[i] == 'R':
                cur = INF
            cur += 1
            l[i] = cur

        for i in range(n):
            if d[i] == 'R':
                cur = -1
            elif d[i] == 'L':
                cur = INF
            cur += 1
            if l[i] < cur:
                ans.append('L')
            elif l[i] > cur:
                ans.append('R')
            else:
                ans.append('.')
        return ''.join(ans)