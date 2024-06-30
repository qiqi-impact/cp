def diam(n, edges):
    adj, visited = [[] for i in range(n + 1)], [0 for i in range(n + 1)]
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
    maxCount = 0
    far = 0
    
    def dfsUtil(node, count):
        nonlocal visited, far, maxCount, adj
        visited[node] = 1
        count += 1
        for i in adj[node]:
            if visited[i] == 0:
                if count >= maxCount:
                    maxCount = count
                    far = i
                dfsUtil(i, count)

    def dfs(node, n):
        count = 0
        for i in range(n + 1):
            visited[i] = 0
        dfsUtil(node, count + 1)

    def diameter(n):
        nonlocal adj, maxCount
        dfs(1, n)
        dfs(far, n)
        return maxCount
    
    return diameter(n) - 1