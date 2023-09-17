class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        ret = 0
        for i in range(k):
            l, r = 0, 10**18
            while l < r:
                mi = (l+r+1)//2
                c = [t*mi for t in composition[i]]
                q = 0
                for j in range(n):
                    c[j] = max(0, c[j] - stock[j])
                    q += c[j] * cost[j]
                if q <= budget:
                    l = mi
                else:
                    r = mi - 1
            ret = max(ret, l)
        return ret