class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        l = [1] + numWays
        r = [1] + [0] * len(numWays)
        ret = []
        for i in range(1, len(r)):
            if l[i] != r[i]:
                if l[i] - r[i] != 1:
                    return []
                ret.append(i)
                for j in range(len(r) - 1, -1, -1):
                    for k in range(j - i, -1, -i):
                        r[j] += r[k]
        return ret©leetcode