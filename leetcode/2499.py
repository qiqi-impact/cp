class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        f = defaultdict(int)
        mx = 0
        mv = 0
        sames = 0
        ret = 0
        
        for i in range(n):
            if nums1[i] == nums2[i]:
                sames += 1
                f[nums1[i]] += 1
                if f[nums1[i]] > mx:
                    mx = f[nums1[i]]
                    mv = nums1[i]
                ret += i
                
        for i in range(n):
            if mx * 2 > sames and nums1[i] != nums2[i] and nums1[i] != mv and nums2[i] != mv:
                ret += i
                sames += 1
                
        return -1 if mx * 2 > sames else ret