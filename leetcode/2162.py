class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def evalpath(p):
            if len(p) == 0:
                return 0
            elif len(p) == 1:
                return p[0]
            elif len(p) == 2:
                return 10 * p[0] + p[1]
            elif len(p) == 3:
                return 60 * p[0] + 10 * p[1] + p[2]
            else:
                return 600 * p[0] + 60 * p[1] + 10 * p[2] + p[3]
            
        def costpath(p):
            cur = startAt
            ret = 0
            for e in p:
                if e != cur:
                    ret += moveCost
                ret += pushCost
                cur = e
            return ret
        
        path = []
        ans = inf
        def dfs(idx):
            nonlocal ans
            if evalpath(path) == targetSeconds:
                ans = min(ans, costpath(path))
            if idx == 4:
                return
            for i in range(10):
                path.append(i)
                dfs(idx+1)
                path.pop()
        dfs(0)
        return ans