class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for i in range(n+1, 1224445):
            s = str(i)
            c = Counter(s)
            fail = False
            for k in c:
                if int(k) != c[k]:
                    fail = True
                    break
            if fail:
                continue
            return i