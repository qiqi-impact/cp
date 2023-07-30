class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ret = 0
        for x in hours:
            if x >= target:
                ret += 1
        return ret