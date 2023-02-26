class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        vis = [0] * n
        j = (n+1)//2
        ret = 0
        for i in range(n):
            if not vis[i]:
                while j < n and (vis[j] or nums[j] < 2 * nums[i]):
                    j += 1
                if j == n:
                    break
                vis[i] = 1
                vis[j] = 1
                ret += 2
        return ret