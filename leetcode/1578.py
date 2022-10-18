class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        last = None
        sm = 0
        mx = 0
        ret = 0
        for i, c in enumerate(colors):
            if c == last:
                sm += neededTime[i]
                mx = max(mx, neededTime[i])
            else:
                if last:
                    ret += sm - mx
                last = c
                sm = mx = neededTime[i]
        if last:
            ret += sm - mx
        return ret