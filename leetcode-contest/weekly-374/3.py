class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        l = [ord(c)-97 for c in word]
        n = len(word)
        ch = [0] * (n+1)
        for i in range(1, n):
            ch[i+1] = ch[i]
            if abs(l[i] - l[i-1]) > 2:
                ch[i+1] += 1
        pf = [[0 for _ in range(26)]]
        for i in range(n):
            pf.append(pf[-1][:])
            pf[i+1][l[i]] += 1
        ret = 0
        for i in range(1, n+1):
            for j in range(k, 27*k, k):
                if i-j < 0:
                    break
                if ch[i] != ch[i-j+1]:
                    break
                r = 1
                kill = 0
                for t in range(26):
                    diff = pf[i][t] - pf[i-j][t]
                    if diff != 0 and diff != k:
                        r = 0
                        break
                    if diff > k:
                        r = 0
                        kill = 1
                        break
                ret += r
                if kill:
                    break
        return ret
                        
                
                