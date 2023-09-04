class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        MX = (1 << n) - 1

        def is_sq(x):
            return pow(int(sqrt(x)), 2) == x

        if n == 1:
            return 1

        @cache
        def dfs(b, lst):
            if b == MX:
                return 1
            ret = 0
            for i in range(n):
                if not (b & (1 << i)) and is_sq(nums[lst] + nums[i]):
                    ret += dfs(b ^ (1 << i), i)
            return ret

        ct = Counter(nums)

        s = sum([dfs(1 << i, i) for i in range(n)])
        for v in ct.values():
            s //= factorial(v)
        return s