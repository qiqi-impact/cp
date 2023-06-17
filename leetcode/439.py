class Solution:
    def parseTernary(self, expression: str) -> str:
        st = []

        def ev():
            e, _, c, _, a = st.pop(), st.pop(), st.pop(), st.pop(), st.pop()
            if a == 'T':
                st.append(c)
            else:
                st.append(e)

        for c in expression:
            if c in 'FT?':
                st.append(c)
            elif c == ':':
                while st[-2] == ':':
                    ev()
                st.append(c)
            else:
                st.append(c)
        while len(st) > 1:
            ev()
        return st[0]