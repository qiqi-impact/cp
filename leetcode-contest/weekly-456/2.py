from sortedcontainers import SortedList

def calc(a, b):
    z = min(len(a), len(b))
    for i in range(z):
        if a[i] != b[i]:
            return i
    return z

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        lcp = {}
        n = len(words)
        for i in range(n):
            for j in range(i+1, min(n, i+3)):
                a, b = words[i], words[j]
                lcp[i,j] = calc(a, b)
        sl = SortedList()
        for i in range(n-1):
            sl.add(lcp[i,i+1])
        ret = []
        for i in range(n):
            if i != n-1:
                sl.discard(lcp[i,i+1])
            if i != 0:
                sl.discard(lcp[i-1,i])
            if i != 0 and i != n-1:
                sl.add(lcp[i-1,i+1])
            ret.append(sl[-1] if sl else 0)
            if i != n-1:
                sl.add(lcp[i,i+1])
            if i != 0:
                sl.add(lcp[i-1,i])
            if i != 0 and i != n-1:
                sl.discard(lcp[i-1,i+1])
        return ret