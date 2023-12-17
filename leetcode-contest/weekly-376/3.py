PAL = []
for i in range(1, 10**5):
    s = str(i)
    a, b = s+s[::-1], s[:-1]+s[::-1]
    for f in a, b:
        PAL.append(int(f))
PAL.sort()

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        nums = [0] + nums
        n = len(nums)
        pt = 0
        opts = []
        for s in PAL:
            while pt < n-1 and nums[pt+1] <= s:
                pt += 1
            opts.append(s)
            if s > nums[-1]:
                break
            if pt > n-1-pt:
                break
        r = inf
        for v in opts[-2:]:
            ans = -v
            for x in nums:
                ans += abs(x - v)
            r = min(r, ans)
        return r
            