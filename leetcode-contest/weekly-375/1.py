class Solution:
    def countTestedDevices(self, bp: List[int]) -> int:
        ret = 0
        n = len(bp)
        for i in range(n):
            if bp[i] > 0:
                ret += 1
                for j in range(i+1, n):
                    bp[j] = max(0, bp[j] - 1)
        return ret