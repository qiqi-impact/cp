class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def can(x):
            ct = 0
            last = -1e9
            for i in range(len(price)):
                if price[i] - last >= x:
                    ct += 1
                    last = price[i]
                    if ct >= k:
                        return True
            return False
        
        l, r = 0, 10**9
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l