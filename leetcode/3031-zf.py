def zf(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(z[i-l], r - i)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        l = zf(word)
        for i in range(0, n, k):
            if l[i] == n-i:
                return i//k
        return (n+k-1)//k