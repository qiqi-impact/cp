class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ret = []
        for i in range(1, n+1):
            s = set(A[:i]) & set(B[:i])
            ret.append(len(s))
        return ret