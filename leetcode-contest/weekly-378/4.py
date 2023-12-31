class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        S = n//2
        l = s[:n//2]
        r = s[n//2:][::-1]
        
        fl = [[0]*26]
        for c in l:
            fl.append(fl[-1][:])
            fl[-1][ord(c)-97] += 1
            
        fr = [[0]*26]
        for c in r:
            fr.append(fr[-1][:])
            fr[-1][ord(c)-97] += 1
            
        sm = [0]
        for i in range(S):
            sm.append(sm[-1] + int(l[i] == r[i]))
        
        def same(i, j):
            if i > j:
                return True
            return sm[j+1] - sm[i] == j-i+1
        
        def count(arr, i, j):
            if i > j:
                return [0] * 26
            return [arr[j+1][k] - arr[i][k] for k in range(26)]
        
        def enough(t, v):
            for i in range(26):
                if t[i] < v[i]:
                    return False
            return True
        
        ret = []
        for a, b, y, x in queries:
            x, y = (n-1)-x, (n-1)-y
            
            if a <= x and y <= b:
                if count(fl, a, b) != count(fr, a, b):
                    ret.append(False)
                    continue
                if not same(0, a-1) or not same(b+1, S-1):
                    ret.append(False)
                    continue
            elif x <= a and b <= y:
                if count(fl, x, y) != count(fr, x, y):
                    ret.append(False)
                    continue
                if not same(0, x-1) or not same(y+1, S-1):
                    ret.append(False)
                    continue
            elif max(a, x) <= min(b, y):
                t, v = min(a, x), max(b, y)
                if count(fl, t, v) != count(fr, t, v):
                    ret.append(False)
                    # print(1)
                    continue
                if not same(0, t-1) or not same(v+1, S-1):
                    ret.append(False)
                    # print(2)
                    continue
                if a <= x:
                    if not enough(count(fl, a, b), count(fr, a, x-1)):
                        ret.append(False)
                        continue
                    if not enough(count(fr, x, y), count(fl, b+1, y)):
                        ret.append(False)
                        continue
                else:
                    if not enough(count(fr, x, y), count(fl, x, a-1)):
                        ret.append(False)
                        continue
                    if not enough(count(fl, a, b), count(fr, y+1, b)):
                        ret.append(False)
                        continue
            else:
                if count(fl, x, y) != count(fr, x, y):
                    ret.append(False)
                    continue
                if count(fl, a, b) != count(fr, a, b):
                    ret.append(False)
                    continue
                if a < x:
                    if not same(0, a-1) or not same(b+1, x-1) or not same(y+1, S-1):
                        ret.append(False)
                        continue
                else:
                    if not same(0, x-1) or not same(y+1, a-1) or not same(b+1, S-1):
                        ret.append(False)
                        continue
            ret.append(True)
        return ret
                
                        
        