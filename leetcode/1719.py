class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        g = defaultdict(list)
        need = set()
        for x, y in pairs:
            g[x].append(y)
            g[y].append(x)
            need.add(x)
            need.add(y)
        l = [(len(g[k]), k) for k in g]
        
        mx = 0
        mxi = None
        for x, y in l:
            if x > mx:
                mx = x
                mxi = y
        
        for k in g:
            g[k].sort(key=lambda x:-len(g[x]))
        vis = set()
        nch = defaultdict(int)
        timer = 0
        
        tin, tout = defaultdict(int), defaultdict(int)
        
        def dfs(idx, anc):
            nonlocal timer
            tin[idx] = timer
            timer += 1
            
            vis.add(idx)
            ct = 0
            anc.add(idx)
            for o in g[idx]:
                if o not in anc:
                    if o in vis and tin[o] < tin[idx]:
                        print(idx, o, tin, tout)
                        return False
                    if o not in vis:
                        nch[idx] += 1
                        if not dfs(o, anc):
                            return False
                else:
                    ct += 1
            anc.discard(idx)
            if ct != len(anc):
                return False
            return True
                    
        if not dfs(mxi, set()): return 0
        if len(vis) != len(need): return 0
        if 1 in nch.values():
            return 2
        return 1