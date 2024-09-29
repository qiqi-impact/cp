class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        pt = [-1] * 7
        ret = 0
        ct = [[0 for _ in range(6)] for _ in range(len(word)+1)]
        for i in range(len(word)):
            for j in range(6):
                ct[i+1][j] = ct[i][j]
            v = word[i]
            if v in 'aeiou':
                t = 'aeiou'.find(v)
                ct[i+1][t] += 1
                while ct[pt[t]+1][t] <= ct[i+1][t] - 1:
                    pt[t] += 1
            else:
                ct[i+1][5] += 1
            if ct[i+1][5] >= k:
                while ct[pt[5]+1][5] <= ct[i+1][5] - k - 1:
                    pt[5] += 1
                while pt[6]+1 < len(ct) and ct[pt[6]+1][5] <= ct[i+1][5] - k:
                    pt[6] += 1
            m = min(pt[:5])
            if m >= 0 and ct[i+1][5] >= k:
                ret += max(0, min(pt[6], m) - pt[5])
            # print(pt)
        # for x in ct:
        #     print(x)
        return ret