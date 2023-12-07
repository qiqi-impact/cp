class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s.replace('a', '$').replace('b', 'a').replace('$', 'b')
            x, y = y, x
        ca, cb = 0, 0
        ret = 0
        for c in s+'$':
            if c == 'a':
                ca += 1
            elif c == 'b':
                if ca:
                    ca -= 1
                    ret += x
                else:
                    cb += 1
            else:
                ret += min(ca, cb)*y
                ca, cb = 0, 0
        return ret