class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            elif len(d) < 2:
                d[x] = 1
            else:
                for k in list(d.keys()):
                    d[k] -= 1
                    if d[k] == 0:
                        del d[k]
        ret = []
        e = defaultdict(int)
        for x in nums:
            if x in d:
                e[x] += 1
        for x in e:
            if e[x] > len(nums) // 3:
                ret.append(x)
        return ret