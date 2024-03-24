class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        h = []
        d = {}
        ret = []
        for i, x in enumerate(nums):
            if x not in d:
                d[x] = [0, -1]
            d[x] = [d[x][0] + freq[i], i]
            while h and h[0][2] != d[h[0][1]][1]:
                heapq.heappop(h)
            heapq.heappush(h, (-d[x][0], x, i))
            if not h:
                ret.append(0)
            else:
                ret.append(-h[0][0])
        return ret