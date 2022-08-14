class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wl = set(wordList)
        if endWord not in wl:
            return []
        wl = [beginWord] + list(wl)
        g = defaultdict(set)
        for a in wl:
            for b in wl:
                fail = 0
                for i in range(len(a)):
                    if a[i] != b[i]:
                        fail += 1
                        if fail == 2:
                            break
                if fail == 1:
                    g[a].add(b)
                    g[b].add(a)
        dst = {beginWord: 0}
        q = deque([beginWord])
        found = False
        while q:
            x = q.popleft()
            for nx in g[x]:
                if nx not in dst:
                    dst[nx] = 1 + dst[x]
                    q.append(nx)
                    if nx == 1:
                        found = True
                        break
            if found:
                break
                
        if endWord not in dst:
            return []
        
        def dfs(w):
            if dst[w] == 0:
                return [[beginWord]]
            r = []
            for o in g[w]:
                if dst.get(o, 1e9) == dst[w] - 1:
                    r += [y + [w] for y in dfs(o)]
            return r
        return dfs(endWord)
                    
        