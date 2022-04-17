class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        class Node:
            nonlocal s
            def __init__(self, i):
                self.v = s[i]
                self.chi = []
        nodes = [Node(i) for i in range(len(s))]
        for i, v in enumerate(parent):
            if v == -1:
                continue
            nodes[v].chi.append(nodes[i])
            
        ret = 1
        def dfs(no):
            nonlocal ret
            best2 = []
            for ch in no.chi:
                x = dfs(ch)
                if ch.v != no.v:
                    best2.append(x)
                    best2.sort(reverse=True)
                    if len(best2) > 2:
                        best2.pop()
            if best2:
                cur = sum(best2) + 1
                ret = max(ret, cur)
            return best2[0]+1 if best2 else 1
        
        dfs(nodes[0])
        return ret