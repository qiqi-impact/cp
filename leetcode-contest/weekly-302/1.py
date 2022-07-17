class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        s = set()
        ret = [0, 0]
        for n in nums:
            if n in s:
                ret[0] += 1
                s.discard(n)
            else:
                s.add(n)
        ret[1] = len(s)
        return ret