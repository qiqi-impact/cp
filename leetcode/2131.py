class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(int)
        for w in words:
            d[w] += 1
        ret = 0
        left = False
        for k in d:
            if k[0] == k[1]:
                ret += 4 * (d[k]//2)
                d[k] %= 2
                if d[k]:
                    left = True
            elif k[1] + k[0] in d:
                v = min(d[k], d[k[1] + k[0]])
                d[k] -= v
                d[k[1] + k[0]] -= v
                ret += 4 * v
        if left:
            ret += 2
        return ret