class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        t = 0
        b = bin(k-1)[2:]
        for i in range(len(b)):
            p = len(b) - i - 1
            if b[i] == '1' and operations[p] == 1:
                t += 1
        return chr(97+(t%26+26)%26)
