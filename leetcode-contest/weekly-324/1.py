class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ret = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if set(words[i]) == set(words[j]):
                    ret += 1
        return ret