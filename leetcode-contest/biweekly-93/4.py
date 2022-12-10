# Solution by tonghuikang

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        c = Counter(nums1 + nums2)
        if max(c.values()) > n:
            return -1

        sames = []
        sames.append(nums1[0])
        sames.append(nums2[0])
        diffs = []
        
        res = 0
        for i,(a,b) in enumerate(zip(nums1[1:], nums2[1:]), start=1):
            if a == b:
                res += i
                sames.append(a)
                sames.append(a)
            else:
                diffs.append(i)
                
        m = len(sames) // 2
        c = Counter(sames)
        maxcnt = max(c.values())
        if maxcnt > m:
            res += sum(diffs[:maxcnt-m])
        
        return res
