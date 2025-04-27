class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        nums = [(x, i) for (i, x) in enumerate(nums)]
        nums.sort()

        m = {}
        for i in range(n):
            m[nums[i][1]] = i

        last = [[None for _ in range(n)] for _ in range(17)]
        j = 0
        for i in range(n):
            while j != n and nums[j][0] - nums[i][0] <= maxDiff:
                j += 1
            last[0][i] = j - 1
        
        for j in range(1, 17):
            for i in range(n):
                last[j][i] = last[j-1][last[j-1][i]]

        def can(x, a, b):
            cur = a
            for j in range(17):
                if x & 1 << j:
                    cur = last[j][cur]
                    if cur >= b:
                        return True
            return False
        
        ret = []
        for x, y in queries:
            a, b = m[x], m[y]
            if a > b:
                a, b = b, a
            if a == b:
                ret.append(0)
                continue
            l, r = 1, n
            while l < r:
                mi = (l + r) // 2
                if can(mi, a, b):
                    r = mi
                else:
                    l = mi + 1
            ret.append(l if l <= n - 1 else -1)
        return ret