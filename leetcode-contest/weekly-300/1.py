class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        i = 0
        for c in key:
            if c not in d and c in ascii_lowercase:
                d[c] = i
                i += 1
        ret = ''
        for c in message:
            if c in d:
                ret += ascii_lowercase[d[c]]
            else:
                ret += c
        return ret