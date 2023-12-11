class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i in [n//4, n//2, 3*n//4]:
            idx = bisect.bisect_left(arr, arr[i])
            if idx + n//4 >= n:
                continue
            if arr[idx + n//4] == arr[idx]:
                return arr[idx]