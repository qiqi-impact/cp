class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                if distance[ord(c)-97] != i - d[c] - 1:
                    return False
        return True