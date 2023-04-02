class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        ret = 0
        for i in range(n):
            ct = [0, 0]
            for j in range(i, n):
                v = int(s[j])
                if v == 0:
                    if ct[1] > 0:
                        break
                    ct[0] += 1
                else:
                    ct[1] += 1
                    if ct[0] == ct[1]:
                        ret = max(ret, sum(ct))
        return ret