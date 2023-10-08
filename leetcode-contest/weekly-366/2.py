class Solution:
    def minProcessingTime(self, p: List[int], t: List[int]) -> int:
        p.sort(reverse=True)
        t.sort()
        ret = 0
        for i in range(3, len(t), 4):
            ret = max(ret, p[i//4] + t[i])
        return ret