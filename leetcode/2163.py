class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        minn = [None] * n
        h = []
        sm = 0
        for i in range(n):
            heapq.heappush(h, -nums[i])
            sm += nums[i]
            if len(h) > n//3:
                sm += heapq.heappop(h)
            if len(h) == n//3:
                minn[i] = sm
        h = []
        sm = 0
        ret = float('inf')
        for i in range(n-1, -1, -1):
            heapq.heappush(h, nums[i])
            sm += nums[i]
            if len(h) > n//3:
                sm -= heapq.heappop(h)
            if len(h) == n//3:
                if i < n//3:
                    break
                ret = min(ret, minn[i-1] - sm)
        return ret