class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        ret = 1
        cur = 1
        while cur <= len(grades):
            ret += 1
            cur += ret
        return ret - 1