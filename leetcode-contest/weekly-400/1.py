class Solution:
    def minimumChairs(self, s: str) -> int:
        st = 0
        mx = 0
        for c in s:
            if c == 'E':
                st += 1
            else:
                st -= 1
            mx = max(mx, st)
        return mx