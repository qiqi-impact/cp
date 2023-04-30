class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        exact = {}
        one = {}
        n = len(nums)
        for i in range(n//2):
            a, b = nums[i], nums[n-1-i]
            if a+b not in exact:
                exact[a+b] = 0
            exact[a+b] += 1
            a, b = min(a, b), max(a, b)
            if a+1 not in one:
                one[a+1] = 0
            one[a+1] += 1
            if b+limit+1 not in one:
                one[b+limit+1] = 0
            one[b+limit+1] -= 1
        ret = inf
        cur = 0
        for sm in range(2, 2*limit+1):
            if sm in one:
                cur += one[sm]
            e = exact.get(sm, 0)
            o = cur - e
            ret = min(ret, o + 2 * (n//2 - o - e))
        return ret