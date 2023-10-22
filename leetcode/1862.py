class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        MX = max(nums)
        freq = [0] * (MX+1)
        for x in nums:
            freq[x] += 1
        pf = [0] * (MX+2)
        for i in range(MX, -1, -1):
            pf[i] = pf[i+1] + freq[i]
        ret = 0
        for i in range(1, MX+1):
            for j in range(MX//i*i, 0, -i):
                v = j//i
                df = 0
                if j+i <= MX:
                    df = pf[j+i]
                ret += v * (pf[j] - df) * freq[i]
            ret %= (10**9+7)
        return ret