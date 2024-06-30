class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k = 2
        nums = [x%k for x in nums]
        mx = 0
        n = len(nums)
        for i in range(k):
            l = [0] * k
            ok = [True] * k
            for x in nums:
                if x == i:
                    for j in range(k):
                        if ok[j]:
                            l[j] += 1
                            if j != i:
                                ok[j] = False
                else:
                    if not ok[x]:
                        ok[x] = True
                        l[x] += 1
            mx = max(mx, max(l))
        return mx