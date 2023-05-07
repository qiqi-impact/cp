class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ret = 0
        a = [0] * n
        ans = []
        
        def test(x):
            return 0 <= x < n-1 and a[x] == a[x+1] and a[x] != 0
        
        for x, y in queries:
            if test(x-1):
                ret -= 1
            if test(x):
                ret -= 1
            a[x] = y
            if test(x-1):
                ret += 1
            if test(x):
                ret += 1
            ans.append(ret)
        return ans