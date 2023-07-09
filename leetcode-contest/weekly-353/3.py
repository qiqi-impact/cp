class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        w = 0
        x = -inf
        y = 0
        z = -inf
        
        ret = 0
        for a, b in zip(nums1, nums2):
            a, b = min(a, b), max(a, b)
            
            nw, nx, ny, nz = 1, b, 1, a
            
            if a >= z:
                ny = y + 1
            if a >= x:
                ny = max(ny, w + 1)
                
            if b >= z:
                nw = y + 1
            if b >= x:
                nw = max(nw, w + 1)
            
            w, x, y, z = nw, nx, ny, nz
            
            ret = max(ret, w, y)
        return ret