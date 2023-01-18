class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ret = 0
        while target > 1:
            if maxDoubles == 0:
                return target - 1 + ret
            ret += 1
            if target%2 == 0:
                maxDoubles -= 1
                target //= 2
            else:
                target -= 1
        return ret