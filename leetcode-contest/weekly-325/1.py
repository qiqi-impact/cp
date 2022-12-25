class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        s = set(words)
        if target not in s:
            return -1
        n = len(words)
        ret = 1e9
        for i in range(n):
            w = words[(startIndex+i)%n]
            if w == target:
                ret = min(ret, i)
        for i in range(n):
            w = words[(startIndex-i)%n]
            if w == target:
                ret = min(ret, i)
        return ret