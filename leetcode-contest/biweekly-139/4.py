class Solution:
    def maxPathLength(self, c: List[List[int]], k: int) -> int:
        tx, ty = c[k]
        a, b = [], []
        for x, y in c:
            if (x < tx and y < ty):
                a.append((x, y))
            if (x > tx and y > ty):
                b.append((x, y))

        def lis2(arr):
            arr.sort(key=lambda x:(x[0], -x[1]))
            lis = []
            for _, y in arr:
                idx = bisect.bisect_left(lis, y)
                if idx == len(lis):
                    lis.append(y)
                else:
                    lis[idx] = y
            return len(lis)
    
        return lis2(a) + lis2(b) + 1