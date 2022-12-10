class Solution:
    def maxJump(self, stones: List[int]) -> int:
        N = len(stones)
        ret = stones[1]
        for i in range(2, N):
            ret = max(ret, stones[i] - stones[i-2])
        return ret
            
            