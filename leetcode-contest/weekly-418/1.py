class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        mx = 0
        for a, b, c in [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]:
            q = [nums[a], nums[b], nums[c]]
            l = [bin(x)[2:] for x in q]
            t = ''.join(l)
            ret = 0
            c = 1
            for i in range(len(t)-1, -1, -1):
                if t[i] == '1':
                    ret += c
                c *= 2
            mx = max(mx, ret)
        return mx