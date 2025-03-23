pw = [1]
for i in range(15):
    pw.append(pw[-1] * 4)

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ret = 0
        for a, b in queries:
            q = 0
            for i in range(len(pw)-1):
                c, d = pw[i], pw[i+1] - 1
                ovr = max(0, min(b, d) - max(a, c) + 1)
                q += ovr * (i + 1)
            ret += (q + 1) // 2
        return ret