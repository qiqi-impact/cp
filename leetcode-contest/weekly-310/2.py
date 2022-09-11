class Solution:
    def partitionString(self, s: str) -> int:
        ret = 1
        x = set()
        for c in s:
            if c in x:
                x = set()
                x.add(c)
                ret += 1
            else:
                x.add(c)
        return ret