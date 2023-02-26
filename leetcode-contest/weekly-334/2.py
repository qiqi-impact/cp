class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        cur = 0
        ret = []
        for c in word:
            cur = (cur * 10 + int(c)) % m
            ret.append(int(cur == 0))
        return ret