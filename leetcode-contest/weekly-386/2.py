class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                a, b, c, d = bottomLeft[i], bottomLeft[j], topRight[i], topRight[j]
                ma0 = max(a[0], b[0])
                ma1 = max(a[1], b[1])
                mc0 = min(c[0], d[0])
                mc1 = min(c[1], d[1])
                
                if ma0 >= mc0 or ma1 >= mc1:
                    continue
                
                ret = max(ret, min((mc1-ma1), (mc0 - ma0)) ** 2)
        return ret