class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ret = 0
        for i in range(len(s)):
            z, o = 0, 0
            for j in range(i, len(s)):
                if s[j] == '1':
                    o += 1
                else:
                    z += 1
                if o <= k or z <= k:
                    ret += 1
        return ret