class Solution:
    def largestVariance(self, s: str) -> int:
        n = len(s)
        ret = 0
        
        idxs = [[] for _ in range(26)]
        for i in range(n):
            idxs[ord(s[i])-97].append(i)
        
        for j in range(26):
            for k in range(j+1, 26):
                pref = [[0,0,0,0]]
                ptr = -1
                
                a = idxs[j]
                b = idxs[k]
                ap = 0
                bp = 0
                while ap < len(a) or bp < len(b):
                    if ap == len(a):
                        c = k
                        bp += 1
                    elif bp == len(b):
                        c = j
                        ap += 1
                    elif a[ap] < b[bp]:
                        c = j
                        ap += 1
                    else:
                        c = k
                        bp += 1
                    r = pref[-1][:]
                    r[0] += int(j == c)
                    r[1] += int(k == c)
                    while 1:
                        nxt = pref[ptr+1]
                        if nxt[0] < r[0] and nxt[1] < r[1]:
                            ptr += 1
                        else:
                            break
                    cur = r[0] - r[1]
                    if ptr != -1:
                        latest = pref[ptr]
                        lmn = latest[2]
                        lmx = latest[3]
                        ret = max(ret, abs(cur - lmn), abs(cur - lmx))
                    r[2] = min(r[2], cur)
                    r[3] = max(r[3], cur)
                    pref.append(r)
        return ret