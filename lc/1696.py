class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [float('inf')] * len(nums)
        dp[-1] = nums[-1]
        q = deque([(nums[-1], len(nums)-1)])
        for i in range(len(nums)-2, -1, -1):
            while q:
                p = q.popleft()
                if p[1] > i+k:
                    continue
                else:
                    q.appendleft(p)
                    mx = p[0]
                    break
            while q:
                p = q.pop()
                if p[0] <= nums[i]+mx:
                    continue
                else:
                    q.append(p)
                    break
            q.append((nums[i]+mx, i))
            dp[i] = nums[i]+mx
        return dp[0]