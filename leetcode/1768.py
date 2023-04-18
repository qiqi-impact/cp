class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = ''
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                ret += word1[i]
            if i < len(word2):
                ret += word2[i]
        return ret