class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ct = defaultdict(int)
        for x in nums:
            ct[x] += 1
        ret = []
        for k in ct:
            if ct[k] == 2:
                ret.append(k)
        return ret