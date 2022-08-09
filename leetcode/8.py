class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        acc = 0
        started = False
        for c in s:
            if c == ' ':
                if started:
                    break
            elif c == '+':
                if started:
                    break
                started = True
            elif c == '-':
                if started:
                    break
                started = True
                neg = True
            elif ord('0') <= ord(c) <= ord('9'):
                started = True
                acc = 10 * acc + int(c)
            else:
                break
        return max(-2**31, min(2**31-1, -acc if neg else acc))