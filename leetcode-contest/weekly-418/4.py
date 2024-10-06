class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        MX = max(nums)
        ct = Counter(nums)
        gcd = [0] * (MX + 1)
        pf = [0] * (MX + 1)

        for i in range(MX, 0, -1):
            old = 0
            for j in range(i, MX + 1, i):
                old += ct[j]
            gcd[i] = old * (old - 1) // 2
            for j in range(i * 2, MX + 1, i):
                gcd[i] -= gcd[j]

        for i in range(1, MX + 1):
            pf[i] = pf[i-1] + gcd[i]

        ret = []
        for q in queries:
            ret.append(bisect_right(pf, q))
        return ret
