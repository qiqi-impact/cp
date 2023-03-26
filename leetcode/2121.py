class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, x in enumerate(arr):
            d[x].append(i)
        ans = [None] * len(arr)
        for x in d:
            sm = sum(d[x])
            cur = 0
            for i, y in enumerate(d[x]):
                ans[y] = i * y - cur + (sm - cur - y) - (len(d[x]) - 1 - i) * y
                cur += y
        return ans