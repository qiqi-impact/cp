class Solution:
    def solve(self, s, k):
        if k <= 1: return 0
        st = set([s])
        q = deque([s])
        ct = 1
        ret = 0
        while q:
            x = q.popleft()
            for j in range(len(x)):
                v = x[:j] + x[j+1:]
                if v not in st:
                    st.add(v)
                    q.append(v)
                    ret += len(s) - len(v)
                    ct += 1
                    if ct == k:
                        return ret
        return -1