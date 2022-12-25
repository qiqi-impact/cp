class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        ct = defaultdict(int)
        for c in s:
            ct[c] += 1
        for x in 'abc':
            if ct.get(x, 0) < k:
                return -1
            ct[x] -= k
        bad = 0
        
        ret = 0
        j = 0
        for i in range(len(s)):
            while j < len(s) and bad == 0:
                c = s[j]
                j += 1
                ct[c] -= 1
                if ct[c] == -1:
                    bad += 1
                if bad == 0:
                    ret = max(ret, j - i)
            if bad == 0:
                ret = max(ret, j - i)
            c = s[i]
            ct[c] += 1
            if ct[c] == 0:
                bad -= 1
        return len(s) - ret