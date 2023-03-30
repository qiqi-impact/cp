class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        l = sorted(list(d.items()), key=lambda x:(x[1], -x[0]))
        ret = []
        for x, y in l:
            ret += [x] * y
        return ret