class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = {}
        for w in words:
            cur = root
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                cur['_'] = cur.get('_', 0) + 1
        ret = [0] * len(words)
        for i, w in enumerate(words):
            cur = root
            for c in w:
                cur = cur[c]
                ret[i] += cur['_']
        return ret