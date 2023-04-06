class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        l, r = [], []
        dl, dr = 0, 0
        
        mni = 0
        
        def diff():
            nonlocal dl, dr
            return (len(l) - dl) - (len(r) - dr)
        
        def burn():
            nonlocal dl, dr, mni
            while r and r[0][1] < mni:
                dr -= 1
                heapq.heappop(r)
            while l and l[0][1] < mni:
                dl -= 1
                heapq.heappop(l)
        
        def rebalance():
            nonlocal dl, dr
            burn()
            while l and r and -l[0][0] > r[0][0]:
                x, y = heapq.heappop(r)
                heapq.heappush(l, (-x,y))
                burn()
            while 1:
                df = diff()
                if df < 0:
                    x, y = heapq.heappop(r)
                    heapq.heappush(l, (-x,y))
                elif df > 1:
                    x, y = heapq.heappop(l)
                    heapq.heappush(r, (-x,y))
                else:
                    break
            burn()
        
        ret = []
        r = [(nums[i], i) for i in range(k)]
        heapq.heapify(r)
        rebalance()
        if k%2:
            ret.append(-l[0][0])
        else:
            ret.append((r[0][0] - l[0][0])/2)
        for i in range(k, len(nums)):
            heapq.heappush(r, (nums[i], i))
            rebalance()
            mni = i-k+1
            rm = i-k
            if l and l[0][1] == i-k:
                heapq.heappop(l)
            elif r and r[0][1] == i-k:
                heapq.heappop(r)
            elif (l and nums[i-k] < -l[0][0]) or (l and nums[i-k] == -l[0][0] and i-k < l[0][1]):
                dl += 1
            else:
                dr += 1
            rebalance()
            if k%2:
                ret.append(-l[0][0])
            else:
                ret.append((r[0][0] - l[0][0])/2)
        return ret