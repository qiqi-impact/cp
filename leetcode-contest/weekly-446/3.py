class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return [n * (n+1) // 2]
        ret = [0] * k
        cur = [0] * k
        ret[0] = 0
        cur[1] = 1
        for x in nums:
            nc = [0] * k
            t = x % k
            for i in range(k):
                j = (i * t) % k
                nc[j] += cur[i]
            cur = nc
            for i in range(k):
                ret[i] += cur[i]
            cur[1] += 1
        return ret