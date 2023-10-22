class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        ct = Counter(nums)
        f = defaultdict(int)
        mn = min(ct.values())
        for k in ct:
            f[ct[k]] += 1
        ans = inf
        s = sorted(f.keys())
        
        for bot in range(mn, 0, -1):
            top = bot+1
            r = 0
            gp = 1
            fail = False
            for k in s:
                gp = max(gp, k//top)
                while gp <= k and not (gp*bot <= k <= gp*top):
                    gp += 1
                if gp == k+1:
                    fail = True
                    break
                # print(k, gp)
                r += gp * f[k]
            if not fail:
                ans = min(ans, r)
                break
        return ans