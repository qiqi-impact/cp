class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        la = [[set() for _ in range(k+1)] for _ in range(n)]
        ra = [[set() for _ in range(k+1)] for _ in range(n)]

        la[0][0].add(0)
        la[0][1].add(nums[0])
        ra[n-1][0].add(0)
        ra[n-1][1].add(nums[n-1])

        for i in range(1, n):
            t = nums[i]
            for j in range(k+1):
                ns = set()
                for x in la[i-1][j]:
                    ns.add(x)
                if j > 0:
                    for x in la[i-1][j-1]:
                        ns.add(x | t)
                la[i][j] = ns

        for i in range(n-2, -1, -1):
            t = nums[i]
            for j in range(k+1):
                ns = set()
                for x in ra[i+1][j]:
                    ns.add(x)
                if j > 0:
                    for x in ra[i+1][j-1]:
                        ns.add(x | t)
                ra[i][j] = ns

        ret = 0
        for i in range(n-1):
            for x in la[i][k]:
                for y in ra[i+1][k]:
                    ret = max(ret, x ^ y)
        return ret
