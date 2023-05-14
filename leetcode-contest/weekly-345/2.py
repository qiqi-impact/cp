class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        cur = 0
        for x in derived:
            cur ^= x
        return cur == 0