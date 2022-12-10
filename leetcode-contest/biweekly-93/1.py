class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ret = 0
        for w in strs:
            try:
                v = int(w)
            except:
                v = len(w)
            ret = max(ret, v)
        return ret