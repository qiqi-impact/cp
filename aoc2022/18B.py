N = 20
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]

s = set()
with open('in') as f:
    for l in f.read().splitlines():
        q = l.split(',')
        q = [int(x) for x in q]
        s.add(tuple(q))
        dp[q[0]][q[1]][q[2]] = 1
q = list(s)

D = []
for i in range(3):
    l = [0, 0, 0]
    for dx in [-1, 1]:
        l[i] = dx
        D.append(tuple(l))



def dfs(i, j, k):
    q = [(i, j, k)]
    qp = 0
    while qp < len(q):
        a, b, c = q[qp]
        for (da, db, dc) in D:
            na, nb, nc = a+da, b+db, c+dc
            if 0 <= na < N and 0 <= nb < N and 0 <= nc < N and dp[na][nb][nc] == 0:
                dp[na][nb][nc] = 1
                q.append((na, nb, nc))
        qp += 1
    return q

dfs(0, 0, 0)
for i in range(N):
    for j in range(N):
        for k in range(N):
            if dp[i][j][k] == 0:
                for x in dfs(i, j, k):
                    s.add(x)

ret = 0
for (a, b, c) in q:
    for da, db, dc in D:
        t = (a + da, b + db, c + dc)
        if t not in s:
            ret += 1
print(ret)