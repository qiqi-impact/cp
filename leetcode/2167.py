class Solution:
    def minimumTime(self, s: str) -> int:
        l = [int(c) for c in s]
        tot = 0
        pref = [0]
        mxpref = [0]
        mx = 0
        for i in range(len(s)):
            pref.append(pref[-1] + (2 * l[i] - 1))
            mxpref.append(max(mxpref[-1], pref[-1]))
            mx = max(mx, pref[-1])
            tot += 2 * l[i]
        cur = 0
        for i in range(len(s)-1, -1, -1):
            cur += 2 * l[i] - 1
            mx = max(mx, mxpref[i] + cur)
        return tot - mx