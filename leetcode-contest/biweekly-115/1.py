class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        st = []
        stp = 0
        ret = []
        for x in words:
            if x == 'prev':
                stp += 1
                if stp > len(st):
                    ret.append(-1)
                else:
                    ret.append(st[-stp])
            else:
                st.append(int(x))
                stp = 0
        return ret