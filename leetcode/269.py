class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        chars = set()
        for w in words:
            for c in w:
                chars.add(c)
        
        g = defaultdict(set)
        
        def dfs(l, r, depth):
            # print(' '*depth + str(l) + ' ' + str(r))
            if l == r:
                return True
            lst = None
            prv = l
            exist = False
            
            for i in range(l, r+1):
                w = words[i]
                if depth >= len(w):
                    if exist:
                        return False
                    continue
                exist = True
                c = w[depth]
                if lst is not None and lst != c:
                    g[lst].add(c)
                    if not dfs(prv, i-1, depth+1):
                        return False
                    prv = i
                lst = c
            if exist:
                if not dfs(prv, r, depth+1):
                    return False
            return True
        
        if not dfs(0, len(words)-1, 0):
            return ''
        
        ind = defaultdict(int)
        for k in g:
            for v in g[k]:
                ind[v] += 1
        ret = ''
        q = deque()
        for k in chars:
            if ind[k] == 0:
                q.append(k)
                ret += k
        while q:
            k = q.popleft()
            for o in g[k]:
                ind[o] -= 1
                if ind[o] == 0:
                    q.append(o)
                    ret += o
        if len(ret) != len(chars):
            return ''
        return ret
                
        