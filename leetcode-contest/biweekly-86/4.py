class Solution:
    def maximumRobots(self, ct: List[int], rc: List[int], b: int) -> int:
        def f(k):
            h = []
            c = 0
            for i in range(k):
                heapq.heappush(h, (-ct[i], i))
                c += rc[i]
            
            if -h[0][0] + k * c <= b:
                return True
            
            for i in range(k, len(ct)):
                while h and h[0][1] <= i - k:
                    heapq.heappop(h)
                heapq.heappush(h, (-ct[i], i))
                c += rc[i] - rc[i - k]
                if -h[0][0] + k * c <= b:
                    return True
            return False
        
        l, r = 0, len(ct)
        while l < r:
            mi = (l+r+1)//2
            if f(mi):
                l = mi
            else:
                r = mi - 1
        return l