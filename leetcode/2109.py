class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ret = ''
        sp = 0
        for i in range(len(s)):
            while sp < len(spaces) and i >= spaces[sp]:
                sp += 1
                ret += ' '
            ret += s[i]
        return ret