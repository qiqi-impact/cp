class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9+7
        h = []
        n, q = len(nums), len(queries)
        for l, r, k, v in queries:
            r -= (r - l) % k
            r += k
            heapq.heappush(h, (l, k, v))
            if r < n:
                heapq.heappush(h, (r, k, pow(v, -1, MOD)))
        ret = 0
        for i in range(n):
            cm = 1
            while h and h[0][0] == i:
                l = h[0][0]
                ck = h[0][1]
                m = 1
                while h and h[0][1] == ck and h[0][0] == i:
                    m *= h[0][2]
                    m %= MOD
                    heapq.heappop(h)
                if l + ck < n:
                    heapq.heappush(h, (l + ck, ck, m))
                cm *= m
                cm %= MOD
            ret ^= (nums[i] * cm) % MOD
        return ret