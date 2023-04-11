class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            ret += [s[i:i+k]]
            if i+k > len(s):
                ret[-1] += fill * (i+k-len(s))
            i += k
        return ret