class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        lcm = [[], []]
        n = len(coins)
        for i in range(1, 1 << n):
            t = None
            ct = 0
            for j in range(n):
                if (i >> j) & 1:
                    if t is None:
                        t = coins[j]
                    else:
                        t = math.lcm(coins[j], t)
                    ct += 1
            lcm[ct%2].append(t)
        
        def can(x):
            q = 0
            for t in lcm[1]:
                q += x // t
            for t in lcm[0]:
                q -= x // t
            return q >= k
        
        l, r = 1, 10**18
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r