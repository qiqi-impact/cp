class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        ct = 0
        cs = ''
        for c in s:
            if c.isdigit():
                ct = 10 * ct + int(c)
            elif c == '[':
                st.append(ct)
                st.append(cs)
                ct, cs = 0, ''
            elif c == ']':
                pcs, pct = st.pop(), st.pop()
                cs = pcs + (cs * pct)
            else:
                cs += c
        return cs