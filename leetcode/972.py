from fractions import Fraction

class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        sd, td = -1, -1
        sf, tf = None, None
        a, b = 0, 0
        for i in range(len(s)):
            if s[i] == '.':
                sd = i
            elif s[i] == '(':
                sf = 0
            elif sf is not None and s[i] != ')':
                sf = 10 * sf + int(s[i])
                a += 1
        for i in range(len(t)):
            if t[i] == '.':
                td = i
            elif t[i] == '(':
                tf = 0
            elif tf is not None and t[i] != ')':
                tf = 10 * tf + int(t[i])
                b += 1
        
        sv, tv = Fraction(0), Fraction(0)
        if sd == -1:
            sv = int(s)
        else:
            p = Fraction(10 ** (sd-1))
            for i in range(len(s)):
                if s[i] == '(':
                    c = Fraction(10*sf, 10**a-1)
                elif s[i] == '.':
                    continue
                else:
                    c = int(s[i])
                sv += p * c
                p *= Fraction(1, 10)
                if s[i] == '(':
                    break

        if td == -1:
            tv = int(t)
        else:
            p = Fraction(10 ** (td-1))
            for i in range(len(t)):
                if t[i] == '(':
                    c = Fraction(10*tf, 10**b-1)
                elif t[i] == '.':
                    continue
                else:
                    c = int(t[i])
                tv += p * c
                p *= Fraction(1, 10)
                if t[i] == '(':
                    break
        return sv == tv