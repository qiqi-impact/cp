class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ret = 0
        for i, w in enumerate(words):
            if left <= i <= right:
                if w[0] in 'aeiou' and w[-1] in 'aeiou':
                    ret += 1
        return ret