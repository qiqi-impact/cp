class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        a = Counter(nums1)
        b = Counter(nums2)
        
        n = len(nums1)
        
        sa = set(nums1)
        sb = set(nums2)
        
        dup = set()
        for x in sa:
            if x in sb:
                dup.add(x)
        dup = len(dup)
        
        
        c = 0
        for k in a:
            c += max(0, a[k]-1)
        left = max(n//2-c, 0)
            
        q = 0
        for k in b:
            q += max(0, b[k]-1)
        left += max(n//2-q, 0)
        
        return len(sa) + len(sb) - max(dup, left)