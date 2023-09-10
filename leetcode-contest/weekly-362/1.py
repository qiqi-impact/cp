class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        vis = set()
        for x, y in nums:
            for i in range(x, y+1):
                vis.add(i)
        return len(vis)