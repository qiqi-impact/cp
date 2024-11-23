class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        dist = {}
        for i in range(26):
            for j in range(26):
                if i == j:
                    dist[i,j] = 0
                    continue
                fcost = 0
                cur = i
                while cur != j:
                    fcost += nextCost[cur]
                    cur = (cur + 1) % 26
                pcost = 0
                cur = i
                while cur != j:
                    pcost += previousCost[cur]
                    cur = (cur - 1) % 26
                dist[i,j] = min(fcost, pcost)
        ret = 0
        for i in range(len(s)):
            a, b = ord(s[i])-97, ord(t[i])-97
            ret += dist[a,b]
        return ret