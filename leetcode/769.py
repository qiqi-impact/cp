class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        taken = [0] * n
        ret = 0
        mx = 0
        for x in arr:
            mx = max(mx, x)
            taken[x] = 1
            if sum(taken[:mx+1]) == mx+1:
                ret += 1
        return ret