class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h = []
        l = sorted(list(zip(capital, profits)))
        lp = 0
        for i in range(k):
            while lp < len(l) and l[lp][0] <= w:
                heapq.heappush(h, -l[lp][1])
                lp += 1
            if not h:
                break
            w -= heapq.heappop(h)
        return w