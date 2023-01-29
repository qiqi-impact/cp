class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        
        l = []
        for i in range(len(weights)-1):
            l.append(weights[i] + weights[i+1])
        l.sort()
        
        return sum(l[-(k-1):]) - sum(l[:k-1])