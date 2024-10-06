class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        mx = 0
        for a, b, c in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]:
            q = [nums[a], nums[b], nums[c]]
            l = [bin(x)[2:] for x in q]
            t = ''.join(l)
            mx = max(mx, int(t, 2))
        return mx