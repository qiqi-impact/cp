class Solution:
    def longestAwesome(self, s: str) -> int:
        parity = 0
        first = defaultdict(int)
        first[0] = -1
        ret = 1        
        for i, c in enumerate(s):
            parity ^= (1 << (ord(c)-ord('0')))
            if parity not in first:
                first[parity] = i
            ret = max(ret, i - first[parity])
            for j in range(26):
                pp = parity ^ (1 << j)
                if pp in first:
                    ret = max(ret, i - first[pp])
        return ret