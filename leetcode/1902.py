from sortedcontainers import SortedList

class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        n = len(order)
        depth = [0] * (n+1)
        sl = SortedList()
        for x in order:
            sl.add(x)
            idx = sl.index(x)
            mx = 1
            for k in [idx-1, idx+1]:
                if 0 <= k < len(sl):
                    mx = max(mx, 1 + depth[sl[k]])
            depth[x] = mx
        return max(depth)