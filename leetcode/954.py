class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        ct = Counter(arr)

        if ct[0] % 2 != 0:
            return False

        for k in sorted(ct.keys(), key=abs):
            ct[2*k] -= ct[k]
            if ct[2*k] < 0:
                return False
        
        return True