class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ret = [0]
        for i in range(len(derived)-1):
            ret.append(derived[i] ^ ret[-1])
        if ret[-1] ^ ret[0] == derived[-1]:
            return True
        ret = [1]
        for i in range(len(derived)-1):
            ret.append(derived[i] ^ ret[-1])
        if ret[-1] ^ ret[0] == derived[-1]:
            return True
        return False