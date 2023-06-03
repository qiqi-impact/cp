class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        seen = set()
        l = []
        for r in grid:
            mxi = 0
            for i in range(len(r)):
                if r[i] == 1:
                    mxi = i
            l.append(mxi)
        ret = 0
        for i in range(len(grid)):
            idx = 0
            found = False
            for j in range(len(grid)):
                if j in seen:
                    continue
                elif l[j] > i:
                    idx += 1
                else:
                    found = True
                    seen.add(j)
                    break
            if not found:
                return -1
            ret += idx
        return ret
            