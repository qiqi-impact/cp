class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d, e = Counter(word1), Counter(word2)
        return sorted(d.values()) == sorted(e.values()) and set(d.keys()) == set(e.keys())