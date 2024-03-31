class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        def MaxDist(A, t):
            minsum, maxsum = inf, -inf
            mindiff, maxdiff = inf, -inf
            W, X, Y, Z = set(), set(), set(), set()

            for i in range(len(A)):
                if i == t:
                    continue
                s = A[i][0] + A[i][1]
                diff = A[i][0] - A[i][1]
                
                if (s < minsum):
                    minsum = s
                    W = set([i])
                elif s == minsum:
                    W.add(i)
                    
                if (s > maxsum):
                    maxsum = s
                    X = set([i])
                elif s == maxsum:
                    X.add(i)
                    
                if (diff < mindiff):
                    mindiff = diff
                    Y = set([i])
                elif diff == mindiff:
                    Y.add(i)
                
                if (diff > maxdiff):
                    maxdiff = diff
                    Z = set([i])
                elif diff == maxdiff:
                    Z.add(i)
            r = max(maxsum - minsum, maxdiff - mindiff)

            return r, minsum, maxsum, mindiff, maxdiff, W, X, Y, Z
        
        r, a, b, c, d, w, x, y, z = MaxDist(points, -1)
        
        cand = w | x | y | z

        ret = inf
        for i in cand:
            ret = min(ret, MaxDist(points, i)[0])
        return ret