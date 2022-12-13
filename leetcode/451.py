class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        l = list(d.items())
        l.sort(key=lambda x:-x[1])
        ret = ''
        for x, y in l:
            ret += x * y
        return ret