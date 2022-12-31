class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ct = len(nums1) + len(nums2)
        
        nums1 += [float('inf')]
        nums2 += [float('inf')]
        
        def f(k, p): #smallest idx of nums1 with >= k total elts less than or equal to nums1[idx] 
            A, B = (nums1, nums2) if not p else (nums2, nums1)
            
            l, r = 0, len(A)-1
            while l < r:
                mi = (l+r)//2
                idx = bisect.bisect_right(B, A[mi])
                if idx + mi + 1 >= k:
                    r = mi
                else:
                    l = mi + 1
            return r
        
        if ct%2 == 1:
            k = (ct+1)//2
            return min(nums1[f(k, 0)], nums2[f(k, 1)])
        else:
            k = ct//2
            a = min(nums1[f(k, 0)], nums2[f(k, 1)])
            b = min(nums1[f(k+1, 0)], nums2[f(k+1, 1)])
            return (a+b)/2
        