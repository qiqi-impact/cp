class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ct = Counter(words)
        ret = 0
        for k in ct:
            if k[0] <= k[1]:
                if k[0] == k[1]:
                    ret += ct[k] // 2
                else:
                    ret += min(ct[k], ct[k[1] + k[0]])
        return ret