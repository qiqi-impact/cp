class Solution:
    def findLatestTime(self, s: str) -> str:
        f = []
        
        for i in range(11, -1, -1):
            x, y = i//10, i%10
            p = s[0:2]
            if p[0] in [str(x), '?'] and p[1] in [str(y), '?']:
                f.append(i)
                break
                
        for i in range(59, -1, -1):
            x, y = i//10, i%10
            p = s[3:5]
            if p[0] in [str(x), '?'] and p[1] in [str(y), '?']:
                f.append(i)
                break
        
        x, y = map(str, f)
        return x.rjust(2, '0') + ':' + y.rjust(2, '0')