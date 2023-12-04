class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        lists = [firstList, secondList]
        pt = [0, 0]
        n = len(lists)
        for i in range(n):
            l = []
            for x, y in lists[i]:
                l += [x, y]
            lists[i] = l
        h = []
        for i in range(n):
            if lists[i]:
                heapq.heappush(h, (lists[i][0], 0, i))
                pt[i] += 1
        ret = []
        st = 0
        while h:
            x, t, i = heapq.heappop(h)
            if t == 0:
                st += 1
                if st == n:
                    ret.append([x, None])
            else:
                st -= 1
                if st == n-1:
                    ret[-1][1] = x
            if pt[i] < len(lists[i]):
                heapq.heappush(h, (lists[i][pt[i]], pt[i]%2, i))
                pt[i] += 1
        return ret