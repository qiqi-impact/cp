class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        st = []
        ret = 0
        for x in nums:
            while st and st[-1][0] < x:
                st.pop()
            if st and st[-1][0] == x:
                st[-1][1] += 1
            else:
                st.append([x, 1])
            ret += st[-1][1]
        return ret