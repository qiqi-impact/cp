class Solution:
    def minOperations(self, k: int) -> int:
        ret = inf
        for i in range(1, int(sqrt(10**5)) + 2):
            ret = min(ret, i-1 + max(0, (k+(i-1))//i - 1))
        return ret