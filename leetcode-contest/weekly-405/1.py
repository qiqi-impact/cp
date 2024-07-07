class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k = k%len(s)
        return s[k:] + s[:k]