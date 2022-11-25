class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ret = []
        sm = 0
        ans = 0
        for a in arr:
            amt = 1
            while ret and ret[-1][0] >= a:
                amt += ret[-1][1]
                sm -= ret[-1][0] * ret[-1][1]
                ret.pop()
            ret.append([a, amt])
            sm += a * amt
            ans += sm
            ans %= int(10**9+7)
        return ans