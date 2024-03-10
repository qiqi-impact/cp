class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        s = sum(apple)
        ct = 0
        while s > 0:
            ct += 1
            s -= capacity[ct-1]
        return ct