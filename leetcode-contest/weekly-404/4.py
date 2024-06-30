class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def diam(edges):
            n = len(edges)+1
            adj, visited = [[] for i in range(n + 1)], [0 for i in range(n + 1)]
            for x, y in edges:
                adj[x].append(y)
                adj[y].append(x)
            maxCount = -10**19
            x = 0
            
            # Sets maxCount as maximum distance from node.
            def dfsUtil(node, count):
                nonlocal visited, x, maxCount, adj
                visited[node] = 1
                count += 1
                for i in adj[node]:
                    if (visited[i] == 0):
                        if (count >= maxCount):
                            maxCount = count
                            x = i
                        dfsUtil(i, count)

            # The function to do DFS traversal. It uses recursive
            # dfsUtil()
            def dfs(node, n):
                count = 0
                for i in range(n + 1):
                    visited[i] = 0

                # Increment count by 1 for visited node
                dfsUtil(node, count + 1)

            # Returns diameter of binary tree represented
            # as adjacency list.
            def diameter(n):
                nonlocal adj, maxCount

                # DFS from a random node and then see
                # farthest node X from it*/
                dfs(1, n)

                # DFS from X and check the farthest node
                dfs(x, n)
                return maxCount
            
            return diameter(n)-1
        
        
        def prune(edges):
            n = len(edges)+1
            g = [set() for _ in range(n)]
            deg = [0 for _ in range(n)]
            q = []
            for x, y in edges:
                g[x].add(y)
                g[y].add(x)
            for i in range(n):
                if len(g[i]) == 1:
                    q.append(i)
            ret = 0
            for i in range(n):
                nq = []
                did = False
                for t in q:
                    if len(g[t]) == 1:
                        for k in g[t]:
                            g[k].discard(t)
                            did = True
                            if len(g[k]) == 1:
                                nq.append(k)
                if did:
                    ret += 1
                if not nq:
                    return ret
                q = nq
            return ret
        
        a = prune(edges1)
        b = prune(edges2)
        print(a, b)
        return max(diam(edges1), diam(edges2), a + b + 1)
        