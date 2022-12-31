class Solution:
    def minDeletions(self, s: str) -> int:
        ct = Counter(s)
        l = sorted(list(ct.values()))
        last = 1e9
        ret = 0
        for i in range(len(l)-1, -1, -1):
            if last == 0:
                cur = 0
            elif l[i] >= last:
                cur = last - 1
            else:
                cur = l[i]
            ret += l[i] - cur
            last = cur
        return ret