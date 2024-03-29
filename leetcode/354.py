class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []
        for _, y in envelopes:
            idx = bisect_left(lis, y)
            if idx == len(lis):
                lis.append(y)
            else:
                lis[idx] = y
        return len(lis)