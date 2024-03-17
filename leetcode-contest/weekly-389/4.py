class Solution:
    def minimumMoves(self, nums: List[int], k: int, mc: int) -> int:
        l = []
        n = len(nums)
        for i in range(len(nums)):
            if nums[i]: l.append(i)
                
        t = sum(l)
        pf = [t]
        ct = 1
        for i in range(1, len(l)):
            df = l[i] - l[i-1]
            pf.append(df * ct - df * (len(l)-ct))
                
        mc = min(mc, k)
        def f(m):
            q = k - m
            if q == 0:
                return 2 * m
            if q > len(l):
                return inf
            
            ret = inf
            sm = 0
            e = q-1
            mid = e//2
            
            for i in range(q):
                if i < mid:
                    sm += l[mid] - l[i]
                else:
                    sm += l[i] - l[mid]
                    
            ret = min(ret, sm)
            
            for i in range(1, len(l) + 1 - q):
                e = i+q-1
                mid = (i+e)//2
                sm += (mid - i - e + mid) * (l[mid] - l[mid-1])
                sm += l[e] - l[mid] + l[i-1] - l[mid-1]
                ret = min(ret, sm)
                
            return ret + 2 * m
                
        ans = inf
        for t in range(mc, mc-4, -1):
            if t >= 0: ans = min(ans, f(t))
        return ans
                
                