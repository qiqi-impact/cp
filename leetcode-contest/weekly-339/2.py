class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        f = Counter(nums)
        ret = []
        i = 1
        while 1:
            cur = []
            for k in f:
                if f[k] >= i:
                    cur.append(k)
            if not cur:
                return ret
            ret.append(cur)
            i += 1