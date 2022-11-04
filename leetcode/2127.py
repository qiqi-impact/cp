class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        rev = [set() for _ in range(n)]
        for i in range(n):
            rev[favorite[i]].add(i)
            
        src = [i for i in range(n) if not rev[i]]
        
        ret = 1
        lv = [None] * n
        doubles = []
        def dfs(i, p, level, it):
            nonlocal ret
            if lv[i] is not None:
                if lv[i][1] == it:
                    ret = max(ret, level - lv[i][0])
                return
            lv[i] = [level, it]
            if favorite[i] == p:
                doubles.append([i, p])
            dfs(favorite[i], i, level + 1, it)
        for x in src:
            dfs(x, -1, 0, x)
        for i in range(n):
            if lv[i] is None:
                dfs(i, -1, 0, i)
        
        def dfs2(i, p):
            mx = 0
            for ch in rev[i]:
                if ch != p:
                    mx = max(mx, 1 + dfs2(ch, i))
            return mx
        
        sm = 0
        for x, y in doubles:
            sm += 2 + dfs2(x, y) + dfs2(y, x)
            
        return max(ret, sm)
        