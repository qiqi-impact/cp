class Solution:
    def similarPairs(self, words: List[str]) -> int:
        bits = defaultdict(int)
        for w in words:
            bm = 0
            for c in w:
                bm |= (1 << (ord(c) - ord('a')))
            bits[bm] += 1
        
        ret = 0
        for k in bits:
            ret += (bits[k]) * (bits[k] - 1) // 2
        return ret