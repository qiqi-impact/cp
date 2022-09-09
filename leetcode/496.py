class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        for i, x in enumerate(nums2):
            d[x] = i
        nr = [None] * len(nums2)
        st = []
        for i in range(len(nums2)-1, -1, -1):
            while st and st[-1] <= nums2[i]:
                st.pop()
            if not st:
                nr[i] = -1
            else:
                nr[i] = st[-1]
            st.append(nums2[i])
        return [nr[d[x]] for x in nums1]