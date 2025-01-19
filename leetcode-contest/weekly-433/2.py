MOD = 10**9+7

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        comb = [[0 for _ in range(k+1)] for _ in range(len(nums)+1)]
        comb[0][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(min(k+1, i+1)):
                comb[i][j] = comb[i-1][j]
                if j > 0:
                    comb[i][j] += comb[i-1][j-1]
                    comb[i][j] %= MOD
        nums.sort()
        ret = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(k):
                if j > i:
                    break
                cur += comb[i][j]
                cur %= MOD
            ret += cur * nums[i]
        ret %= MOD
        nums.sort(reverse=True)
        for i in range(len(nums)):
            cur = 0
            for j in range(k):
                if j > i:
                    break
                cur += comb[i][j]
                cur %= MOD
            ret += cur * nums[i]
        ret %= MOD
        return ret