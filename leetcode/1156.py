class Solution:
    def maxRepOpt1(self, text: str) -> int:
        freq = defaultdict(int)
        for x in text:
            freq[x] += 1
        
        ret = 1
        n = len(text)
        for i in range(1, n-1):
            if text[i-1] == text[i+1] and text[i-1] != text[i]:
                v = text[i-1]
                sz = 1
                for j in range(i-1, -1, -1):
                    if text[j] == v:
                        sz += 1
                    else:
                        break
                for j in range(i+1, n):
                    if text[j] == v:
                        sz += 1
                    else:
                        break
                sz = min(sz, freq[v])
                ret = max(ret, sz)
                
        cur = 1
        for i in range(1, n):
            if text[i] == text[i-1]:
                cur += 1
            else:
                cur = 1
            ret = max(ret, cur + int(freq[text[i]] > cur))
        return ret