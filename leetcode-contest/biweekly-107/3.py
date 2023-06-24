class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        @cache
        def dp(idx, left, right):
            if idx == len(words):
                return 0
            w = words[idx]
            l, r = words[idx][0], words[idx][-1]
            return min(len(w)-1 + int(r != left) + dp(idx+1, l, right), len(w)-1 + int(l != right) + dp(idx+1, left, r))
        return len(words[0]) + dp(1, words[0][0], words[0][-1])