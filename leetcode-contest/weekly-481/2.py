class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += cost[i]
        return sum(cost) - max(d.values())