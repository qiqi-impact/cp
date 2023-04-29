class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        
        def can(x):
            ret = 0
            cur = 0
            for t in bloomDay:
                if t <= x:
                    cur += 1
                    if cur == k:
                        cur = 0
                        ret += 1
                        if ret >= m:
                            return True
                else:
                    cur = 0
            return False

        l, r = 1, max(bloomDay)
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r

        