class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        a = [str(x) for x in arr1]
        b = [str(x) for x in arr2]
        
        def can(x):
            d = set()
            for t in a:
                if len(t) >= x:
                    d.add(t[:x])
            for t in b:
                if len(t) >= x and t[:x] in d:
                    return True
            return False   
        
        l, r = 0, 10
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l