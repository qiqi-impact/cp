class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        pref = [0]
        for i in range(n):
            pref.append(pref[-1] + nums[i])
        best1left = [-inf for _ in range(n)]
        best2left = [-inf for _ in range(n)]
        best1right = [-inf for _ in range(n)]
        best2right = [-inf for _ in range(n)]

        cur = -inf
        for i in range(firstLen-1, n):
            cur = max(cur, pref[i+1] - pref[i+1-firstLen])
            best1left[i] = cur
            
        cur = -inf
        for i in range(secondLen-1, n):
            cur = max(cur, pref[i+1] - pref[i+1-secondLen])
            best2left[i] = cur
            
        cur = -inf
        for i in range(n-firstLen, -1, -1):
            cur = max(cur, pref[i+firstLen] - pref[i])
            best1right[i] = cur
            
        cur = -inf
        for i in range(n-secondLen, -1, -1):
            cur = max(cur, pref[i+secondLen] - pref[i])
            best2right[i] = cur
            
        ret = -inf
        for i in range(n-1):
            ret = max(ret, best1left[i] + best2right[i+1], best2left[i] + best1right[i+1])
        return ret