class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        cc = [-1 for _ in range(n)]
        step = 0
        for i in range(n):
            if cc[i] == -1:
                cc[i] = step
                for j in range(i+1, n):
                    if lcp[i][j] != 0:
                        if cc[j] != -1:
                            return ''
                        cc[j] = step
                step += 1
                step %= 26
        for i in range(n):
            for j in range(n):
                if cc[i] == cc[j]:
                    prev = 0
                    if i < n-1 and j < n-1:
                        prev = lcp[i+1][j+1]
                    if lcp[i][j] != 1 + prev:
                        return ''
                else:
                    if lcp[i][j] != 0:
                        return ''
        return ''.join([chr(97+x) for x in cc])
