class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        for a in arrays:
            for e in a:
                d[e] += 1
        ret = []
        for k in d:
            if d[k] == len(arrays):
                ret.append(k)
        return sorted(ret)