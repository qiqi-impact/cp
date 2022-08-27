class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        g = defaultdict(set)
        ind = [0] * n
        for x, y in relations:
            g[x-1].add(y-1)
            ind[y-1] += 1
                
        FULL = (1 << n) - 1
        
        @cache
        def dfs(taken):
            if taken == FULL:
                return 0
            l = []
            for i in range(n):
                if not (taken & (1 << i)) and ind[i] == 0:
                    l.append(i)
            ret = float('inf')
            for x in combinations(l, min(k, len(l))):
                new_taken = taken
                for y in x:
                    new_taken |= (1 << y)
                    for other in g[y]:
                        ind[other] -= 1
                ret = min(ret, 1 + dfs(new_taken))
                for y in x:
                    for other in g[y]:
                        ind[other] += 1
            return ret
               
        return dfs(0)