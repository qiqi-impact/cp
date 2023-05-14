class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ret = [0]
        for i in range(len(derived)-1):
            ret.append(derived[i] ^ ret[-1])
        return ret[-1] ^ ret[0] == derived[-1]