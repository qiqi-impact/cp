class Solution:
    def survivedRobotsHealths(self, p: List[int], h: List[int], d: str) -> List[int]:
        n = len(p)
        pp = sorted(list(range(n)), key=lambda x:p[x])
        st = []
        for i in pp:
            if d[i] == 'R':
                st.append(i)
            else:
                while st and h[i]:
                    a = 0 if h[st[-1]] <= h[i] else h[st[-1]]-1
                    b = 0 if h[st[-1]] >= h[i] else h[i]-1
                    h[st[-1]] = a
                    h[i] = b
                    if st and h[st[-1]] == 0:
                        st.pop()
        return [x for x in h if x != 0]