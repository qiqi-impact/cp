class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        l = [int(x%modulo==k) for x in nums]
        ret = 0
        cur = 0
        d = {0: 1}
        for x in l:
            cur += x
            cur %= modulo
            ret += d.get((cur-k)%modulo, 0)
            d[cur] = d.get(cur, 0) + 1
        return ret