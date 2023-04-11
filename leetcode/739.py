class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ret = [0] * n
        st = []
        for i in range(n-1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            if st:
                ret[i] = st[-1] - i
            st.append(i)
        return ret