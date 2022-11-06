class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        lp = 0
        rp = len(costs)-1
        
        h = []
        
        ret = 0
        for i in range(candidates):
            if lp <= rp:
                heapq.heappush(h, (costs[lp], lp))
                lp += 1
            if lp <= rp:
                heapq.heappush(h, (costs[rp], rp))
                rp -= 1
        
        while k:
            k -= 1
            x, y = heapq.heappop(h)
            ret += x
            if y < lp:
                if lp <= rp:
                    heapq.heappush(h, (costs[lp], lp))
                    lp += 1
            else:
                if lp <= rp:
                    heapq.heappush(h, (costs[rp], rp))
                    rp -= 1
        return ret