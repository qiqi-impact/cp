class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        ret = 0
        for i in range(n):
            ret += prices[i] * strategy[i]
        tot = ret
        for i in range(k // 2):
            tot += prices[i] * (0 - strategy[i])
        for i in range(k // 2, k):
            tot += prices[i] * (1 - strategy[i])
        ret = max(ret, tot)
        for j in range(k, n):
            tot += prices[j] * (1 - strategy[j])
            tot += prices[j - k // 2] * -1
            tot += prices[j - k] * (strategy[j - k] - 0)
            ret = max(ret, tot)
        return ret