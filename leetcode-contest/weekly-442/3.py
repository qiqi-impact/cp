class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        ed = [0] * n
        cur = 0
        for i in range(m):
            if i > 0:
                mx = ed[0]
                c = 0
                for j in range(1, n):
                    c += skill[j-1] * mana[i]
                    mx = max(mx, ed[j] - c)
                cur = mx
            for j in range(n):
                cur += skill[j] * mana[i]
                ed[j] = cur
        return ed[-1]
            