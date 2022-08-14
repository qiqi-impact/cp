class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        inc = [0] * len(edges)
        for i in range(len(edges)):
            inc[edges[i]] += i
        mx = float('-inf')
        mxi = None
        for i in range(len(inc)):
            if inc[i] > mx:
                mx = inc[i]
                mxi = i
        return mxi