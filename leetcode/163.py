class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def tostr(a, b):
            if a == b:
                return str(a)
            else:
                return str(a) + '->' + str(b)
        
        nxt = lower
        ret = []
        for n in nums + [upper+1]:
            if n == nxt:
                nxt += 1
            else:
                ret.append(tostr(nxt, n - 1))
                nxt = n + 1
        return ret