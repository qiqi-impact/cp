class Solution:
    def kthPalindrome(self, queries: List[int], L: int) -> List[int]:
        r = 9 * (10 ** ((L-1)//2))
        ret = []
        for q in queries:
            if q > r:
                ret.append(-1)
                continue
            cq = q + (10 ** ((L-1)//2)) - 1
            s = str(cq)
            st = len(s)-1
            if L % 2 == 1:
                st -= 1
            for i in range(st, -1, -1):
                s += s[i]
            ret.append(s)
        return ret