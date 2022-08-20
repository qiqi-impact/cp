class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            j = 0
            nx = []
            did = False
            while j < n:
                if s[j] == '0':
                    if j == n-1 or s[j+1] == '0':
                        nx.append(s[j])
                    else:
                        nx.append('10')
                        j += 1
                        did = True
                else:
                    nx.append(s[j])
                j += 1
            if not did:
                return i
            s = ''.join(nx)
        return n