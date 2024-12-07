def getMaxRequests(serverCapacity, incomingRequests, k):
    n = len(serverCapacity)
    diff = []
    sm = 0
    for i in range(n):
        a, b = serverCapacity[i], incomingRequests[i]
        diff.append(min(2 * a, b) - min(a, b))
        sm += min(a, b)
    diff.sort(reverse=True)
    return sm + diff[:k]