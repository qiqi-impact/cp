from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ret = []
        for i in range(len(nums)-k+1):
            d = defaultdict(int)
            for j in range(i, i+k):
                d[nums[j]] += 1
            l = sorted([(d[t], t) for t in d])
            cur = 0
            for q in range(max(0, len(l)-x), len(l)):
                cur += l[q][0] * l[q][1]
            ret.append(cur)
        return ret
