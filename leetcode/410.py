class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        pref = [0]
        for n in nums:
            pref.append(pref[-1] + n)
            
        def can(x):
            cur = 0
            for i in range(m):
                v = pref[cur] + x
                idx = bisect.bisect_right(pref, v)
                if idx == len(pref):
                    return True
                if pref[idx] > v:
                    idx -= 1
                cur = idx
            return False
            
        l, r = 0, 10**9
        while l < r:
            mi = (l+r)//2
            v = can(mi)
            if v:
                r = mi
            else:
                l = mi+1
        return l