class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        ct = 0
        for i in range(n):
            if nums[i] == -1:
                ct += 1

        ans = 0
        for i in range(n-1):
            if nums[i+1] != -1 and nums[i] != -1:
                ans = max(ans, abs(nums[i+1] - nums[i]))
                
        def can(x):
            ranges = []
            for i in range(n):
                if nums[i] == -1:
                    mn, mx = -inf, inf
                    if i > 0 and nums[i-1] != -1:
                        mn = max(mn, nums[i-1] - x)
                        mx = min(mx, nums[i-1] + x)
                    if i < n-1 and nums[i+1] != -1:
                        mn = max(mn, nums[i+1] - x)
                        mx = min(mx, nums[i+1] + x)
                    ranges.append([mx, mn, i])
                    if mn > mx:
                        return False
            
            r = []
            cap = {}
            ranges.sort()
            used = set()
            rm = {}
            for yy, xx, i in ranges:
                rm[i] = [xx, yy]
            cur = -inf
            while ranges:
                yy, xx, i = heapq.heappop(ranges)
                if i in used:
                    continue
                used.add(i)
                if yy < xx:
                    return False
                if cur < xx:
                    if len(r) == 2:
                        return False
                    cur = yy
                    r.append(cur)
                if i < n-1 and nums[i+1] == -1 and i+1 not in used:
                    a, b = rm[i+1]
                    heapq.heappush(ranges, [min(cur+x, b), max(cur-x, a), i+1])
                    rm[i+1] = [max(cur-x, a), min(cur+x, b)]
                if i > 0 and nums[i-1] == -1 and i-1 not in used:
                    a, b = rm[i-1]
                    heapq.heappush(ranges, [min(cur+x, b), max(cur-x, a), i-1])
                    rm[i-1] = [max(cur-x, a), min(cur+x, b)]
            return True
        l, r = ans, 10**9
        while l < r:
            mi = (l + r) // 2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r
                    
            