class Solution:
    def maximumSumOfHeights(self, m: List[int]) -> int:
        n = len(m)
        l = [None] * n
        r = [None] * n
        
        st = []
        cur = 0
        for i in range(n):
            v = [m[i], 1]
            cur += v[0]
            while st and st[-1][0] > v[0]:
                x, y = st.pop()
                v[1] += y
                cur -= x * y
                cur += v[0] * y
            l[i] = cur
            st.append(v)
        st = []
        cur = 0
        for i in range(n-1, -1, -1):
            v = [m[i], 1]
            cur += v[0]
            while st and st[-1][0] > v[0]:
                x, y = st.pop()
                v[1] += y
                cur -= x * y
                cur += v[0] * y
            r[i] = cur
            st.append(v)
        # print(l, r)
        ret = max([l[i] + r[i] - m[i] for i in range(n)])
        return ret