class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l = [n for n in nums if n%6==0]
        if not l: return 0
        return sum(l)//len(l)