class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def gt(x):
            return int(x[:2]) * 60 + int(x[3:])
        a, b = list(map(gt, event1)), list(map(gt, event2))
        for i in range(24*60):
            if a[0] <= i <= a[1] and b[0] <= i <= b[1]:
                return True
        return False