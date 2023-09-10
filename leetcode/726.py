class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st = ['(']
        for c in formula + ')':
            if c == '(':
                st.append(c)
            elif c in string.ascii_uppercase:
                st.append([{c: 1}, 0])
            elif c in string.ascii_lowercase:
                for k in list(st[-1][0].keys()):
                    st[-1][0] = {k+c: 1}
            elif c in string.digits:
                x = int(c)
                st[-1][1] = 10 * st[-1][1] + x
            elif c == ')':
                fr = {}
                while st[-1] != '(':
                    x, y = st[-1]
                    for k in x:
                        fr[k] = fr.get(k, 0) + x[k] * max(1, y)
                    st.pop()
                st.pop()
                st.append([fr, 0])
        ret = ''
        for k in sorted(st[0][0].keys()):
            ret += k
            if st[0][0][k] > 1:
                ret += str(st[0][0][k])
        return ret