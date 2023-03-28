class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ''
        for i in range(1+min([len(x) for x in strs])):
            for w in strs:
                if len(w) == i or w[i] != strs[0][i]:
                    return ret
            ret += w[i]