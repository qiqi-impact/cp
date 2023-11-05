class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ind = [1] * n
        for x, y in edges:
            ind[y] = 0
        if sum(ind) > 1:
            return -1
        for i in range(n):
            if ind[i]:
                return i