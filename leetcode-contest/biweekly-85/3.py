class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        ls = [0] * (n+1)
        for a, b, c in shifts:
            df = 1 if c == 1 else -1
            ls[a] += df
            ls[b+1] -= df
        ret = [ord(c)-97 for c in s]
        cur = 0
        for i, c in enumerate(ret):
            cur += ls[i]
            ret[i] = chr(97+((c+cur)%26+26)%26)
        return ''.join(ret)