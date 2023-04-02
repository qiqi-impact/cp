from sortedcontainers import SortedList

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        sb = set(banned)
        ret = [-1] * n
        ret[p] = 0
        
        sls = [SortedList(), SortedList()]
        for i in range(n):
            if i not in sb:
                sls[i%2].add(i)

        q = deque([p])
        while q:
            v = q.popleft()
            l = max(v - (k-1), 0)
            r = min(v + (k-1), n-1)
            nv = 2 * l + k - 1 - v
            mx = 2 * r - k + 1 - v
            
            sl = sls[v%2] if k%2 else sls[1-v%2]
            
            idx = sl.bisect_left(nv)
            while idx < len(sl) and sl[idx] <= mx:
                if ret[sl[idx]] == -1:
                    ret[sl[idx]] = ret[v] + 1
                    q.append(sl[idx])
                del sl[idx]
        return ret