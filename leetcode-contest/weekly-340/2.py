class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
            
        ret = [0] * len(nums)
        for k in d:
            s = sum(d[k])
            x = 0
            for i in range(len(d[k])):
                v = d[k][i]
                x += v
                ret[v] = v * (i + 1) - x + (s - x) - v * (len(d[k]) - (i+1))
        return ret