from typing import List
import bisect

class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        a = sorted(arr)
        pf = [0]
        for x in a:
            pf.append(pf[-1] + x)
        ret = []
        for i, x in enumerate(arr):
            idx = bisect.bisect_left(a, x)
            ret.append(pf[idx])
        return ret