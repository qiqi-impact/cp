class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tp = 0
        for c in s:
            if tp == len(t):
                return 0
            if t[tp] == c:
                tp += 1
        return len(t) - tp