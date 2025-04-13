class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ct = Counter(s)
        center = ''
        for k in ct:
            if ct[k] % 2:
                ct[k] -= 1
                center = k
        ret = ''
        for c in string.ascii_lowercase:
            if ct[c]:
                ret += c * (ct[c] // 2)
        return ret + center + ret[::-1]©leetcode