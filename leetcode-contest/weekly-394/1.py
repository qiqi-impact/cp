class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        U, L = string.ascii_uppercase, string.ascii_lowercase
        s = set(word)
        ret = 0
        for i in range(26):
            if L[i] in s and U[i] in s:
                ret += 1
        return ret