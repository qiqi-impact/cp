class Solution:
    def maximumSumOfHeights(self, m: List[int]) -> int:
        n = len(m)
        mx = 0
        for i in range(n):
            cur = m[i]
            sm = cur
            t = cur
            for j in range(i-1, -1, -1):
                t = min(t, m[j])
                sm += t
            t = cur
            for j in range(i+1, n):
                t = min(t, m[j])
                sm += t
            mx = max(mx, sm)
        return mx