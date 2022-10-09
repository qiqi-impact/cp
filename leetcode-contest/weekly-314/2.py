class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        pref = [0] + pref
        ret = []
        for i in range(1, len(pref)):
            ret.append(pref[i] ^ pref[i-1])
        return ret