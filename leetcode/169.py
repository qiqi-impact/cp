class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                if len(d) < 1:
                    d[x] = 1
                else:
                    for k in list(d.keys()):
                        d[k] -= 1
                        if d[k] == 0:
                            del d[k]
        ct = defaultdict(int)
        for x in nums:
            if x in d:
                ct[x] += 1
                if ct[x] > len(nums)//2:
                    return x
                        