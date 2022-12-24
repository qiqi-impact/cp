l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# pf = [0]
# for x in l:
#     pf.append(pf[-1] + x)
# print(pf)

# mn = float('inf')
# ret = 0
# for x in pf:
#     ret = max(ret, x - mn)
#     mn = min(mn, x)
# print(ret)

n = len(l)
lm = 0
gm = float('-inf')
for i in range(n):
    lm = l[i] + max(0, lm)
    gm = max(gm, lm)
print(gm)