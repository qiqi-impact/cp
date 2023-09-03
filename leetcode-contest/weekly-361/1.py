class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ret = 0
        for i in range(low, high+1):
            l = [int(x) for x in str(i)]
            if len(l)%2:
                continue
            t = len(l)
            ret += (sum(l[:t//2]) == sum(l[t//2:]))
        return ret