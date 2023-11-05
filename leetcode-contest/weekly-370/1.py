class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        l = [sum(grid[i]) for i in range(len(grid))]
        for i in range(len(l)):
            if l[i] == len(grid)-1:
                return i
