from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        q = deque()
        
        def add(i):
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
        
        for i in range(k):
            add(i)
        ret.append(q[0][0])
        for i in range(k, len(nums)):
            add(i)
            while q[0][1] <= i-k:
                q.popleft()
            ret.append(q[0][0])
        return ret