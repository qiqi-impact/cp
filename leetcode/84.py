class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        n = len(heights)
        ret = 0
        for i, h in enumerate(heights):
            ni = i
            while st and st[-1][0] > h:
                ret = max(ret, (i - st[-1][1]) * st[-1][0])
                ni = st[-1][1]
                st.pop()
            st.append((h, ni))
        for h, i in st:
            ret = max(ret, (n - i) * h)
        return ret