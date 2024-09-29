class Solution:
    def kthCharacter(self, k: int) -> str:
        w = 'a'
        while len(w) < k:
            w += ''.join([chr(97+(ord(c)-97+1)%26) for c in w])
        return w[k-1]