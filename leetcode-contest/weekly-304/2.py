class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        for i in range(100000):
            if i*(i+1)//2>len(grades):
                return i-1