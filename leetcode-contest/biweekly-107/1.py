class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set()
        ret = 0
        for w in words:
            if w[0] != w[1]:
                if w[1] + w[0] in s:
                    s.discard(w[1] + w[0])
                    ret += 1
                else:
                    s.add(w)
        return ret