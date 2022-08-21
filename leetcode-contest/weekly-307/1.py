class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ret = max(0, sum(energy) + 1 - initialEnergy)
        cur = initialExperience
        for x in experience:
            if cur <= x:
                ret += x+1-cur
                cur = x+1
            cur += x
        return ret