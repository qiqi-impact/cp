class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        R, C = len(seats), len(seats[0])

        st = []
        for l in seats:
            cur = 0
            for i in range(C):
                if l[i] == '.':
                    cur ^= 1 << i
            st.append(cur)

        valid = []
        for i in range(2**C):
            fail = 0
            for j in range(1, C):
                if (1 & (i >> j)) and (1 & (i >> (j-1))):
                    fail = 1
                    break
            if not fail:
                valid.append(i)

        m = {}
        for i in valid:
            m[i] = []
            for j in valid:
                fail = 0
                for k in range(C):
                    if 1 & (i >> k):
                        if k > 0 and (1 & (j >> (k-1))):
                            fail = 1
                            break
                        if k < C-1 and (1 & (j >> (k+1))):
                            fail = 1
                            break
                if not fail:
                    m[i].append(j)

        @cache
        def dp(idx, last):
            if idx == R:
                return 0
            ret = 0
            for t in m[last]:
                if t & st[idx] == t:
                    ret = max(ret, t.bit_count() + dp(idx+1, t))

            return ret

        return dp(0, 0)
            