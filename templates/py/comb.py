MX = 1001
MOD = 10**9+7
comb = [[0 for _ in range(MX+1)] for _ in range(MX+1)]
comb[0][0] = 1
for i in range(1, MX+1):
    for j in range(i+1):
        if j > 0:
            comb[i][j] += comb[i-1][j-1]
        comb[i][j] += comb[i-1][j]
        comb[i][j] %= MOD