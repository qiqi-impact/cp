class Solution:
    def uniqueLetterString(self, s: str) -> int:
        indices = [[-1] for _ in range(26)]
        for i, c in enumerate(s):
            indices[ord(c)-ord('A')].append(i)
        ret = 0
        for i in range(26):
            indices[i].append(len(s))
            for j in range(1, len(indices[i])-1):
                ret += (indices[i][j] - indices[i][j-1]) * (indices[i][j+1] - indices[i][j])
        return ret