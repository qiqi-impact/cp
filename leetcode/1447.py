class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        d = {0: -1}
        cur = 0
        left = []
        mn = inf
        for i in range(len(arr)-1):
            x = arr[i]
            cur += x
            if cur - target in d:
                mn = min(mn, i - d[cur - target])
            d[cur] = i
            left.append(mn)
        cur = 0
        d = {0: len(arr)}
        mn = inf
        ret = inf
        for i in range(len(arr)-1, 0, -1):
            x = arr[i]
            cur += x
            if cur - target in d:
                mn = min(mn, d[cur - target] - i)
            d[cur] = i
            ret = min(ret, mn + left[i-1])
        return ret if ret != inf else -1