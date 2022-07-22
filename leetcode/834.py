class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = [[0, 1, set()] for _ in range(n)]
        '''
        nodes[idx][0] = sum of dist from idx to everything in its subtree
        nodes[idx][1] = number of vertices in its subtree
        nodes[idx][2] = adjacent vertices in graph
        '''
        
        for x, y in edges:
            nodes[x][2].add(y)
            nodes[y][2].add(x)
        
        def dfs(node, p):
            cur = nodes[node]
            for ch in cur[2]:
                if ch != p:
                    dfs(ch, node)
                    cur[1] += nodes[ch][1]
                    cur[0] += nodes[ch][0] + nodes[ch][1]
            
        ret = [None for _ in range(n)]
        def f(node, p):
            ret[node] = ret[p] + nodes[0][1] - 2 * nodes[node][1]
            for ch in nodes[node][2]:
                if ch != p:
                    f(ch, node)
            
        dfs(0, -1)
        ret[0] = nodes[0][0]
        for ch in nodes[0][2]:
            f(ch, 0)
        return ret