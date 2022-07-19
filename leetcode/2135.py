class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        bits = set()
        for w in startWords:
            b = 0
            for c in w:
                b |= 1 << (ord(c)-97)
            bits.add(b)
        ret = 0
        for w in targetWords:
            b = 0
            for c in w:
                b |= 1 << (ord(c)-97)
            for i in range(26):
                if b & (1 << i):
                    bb = b ^ (1 << i)
                    if bb in bits:
                        ret += 1
                        break
        return ret