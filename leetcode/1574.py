class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        brk = None
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                brk = i+1
                break
        if brk is None:
            return 0
        ret = brk

        t = arr[brk:]

        prv = -inf
        for i in range(len(arr)):
            if prv > arr[i]:
                break
            idx = brk + bisect.bisect_left(t, arr[i])
            ret = min(ret, idx - i - 1)
            prv = arr[i]
        return ret