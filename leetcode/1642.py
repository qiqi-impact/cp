class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        
        l = []
        for i in range(len(heights)-1):
            l.append(heights[i+1] - heights[i])
            
        b = 0
        for i, x in enumerate(l):
            if x > 0:
                heapq.heappush(h, x)
                if len(h) > ladders:
                    b += heapq.heappop(h)
                    if b > bricks:
                        return i
        return len(heights)-1