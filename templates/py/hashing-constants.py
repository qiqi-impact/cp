MX = 10**5 + 5
MOD = 10**9+3
base = 87
base_pow = [1] * (MX + 1)
for i in range(MX):
    base_pow[i+1] = base_pow[i] * base % MOD