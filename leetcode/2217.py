class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        d = (intLength+1)//2
        amt = 9 * (10 ** (d-1))
        ret = []
        for q in queries:
            if q > amt:
                ret.append(-1)
                continue
            s = str((10**(d-1)) + q - 1)
            rs = s[::-1]
            if intLength%2 == 1:
                s = s[:-1]
            ret.append(int(s + rs))
        return ret