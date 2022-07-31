class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        idxs = []
        seen = set()
        double = False
        for i in range(len(s)):
            if s[i] != goal[i]:
                idxs.append(i)
            if s[i] in seen:
                double = True
            else:
                seen.add(s[i])
        if double and len(idxs) == 0:
            return True
        if len(idxs) != 2:
            return False
        return s[idxs[0]] == goal[idxs[1]] and s[idxs[1]] == goal[idxs[0]]