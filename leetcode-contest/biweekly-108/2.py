class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        s = set(nums)
        for i in range(len(moveFrom)):
            a, b = moveFrom[i], moveTo[i]
            if a in s:
                s.discard(a)
                s.add(b)
        return sorted(s)