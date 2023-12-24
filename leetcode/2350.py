class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        ret = 1
        s = set()
        for n in rolls:
            s.add(n)
            if len(s) == k:
                s = set()
                ret += 1
        return ret