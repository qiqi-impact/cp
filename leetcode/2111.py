class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        ret = 0
        for md in range(k):
            lis = []
            ct = 0
            for i in range(md, len(arr), k):
                ct += 1
                v = arr[i]
                idx = bisect.bisect(lis, v)
                if idx == len(lis):
                    lis.append(v)
                else:
                    lis[idx] = v
            ret += ct - len(lis)
        return ret