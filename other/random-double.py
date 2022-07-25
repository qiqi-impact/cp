import random, collections

A = [[random.random() for _ in range(1000)] for _ in range(200)]
B = [[random.random() for _ in range(1000)] for _ in range(100)]

# def chk_equal(i, j):
    # for k in range(1000):
    #     if A[i][k] != B[j][k]:
    #         return False
    # return True

a_indices = random.sample(list(range(200)), 50)
b_indices = random.sample(list(range(100)), 50)

for i in range(50):
    A[a_indices[i]] = B[b_indices[i]]

cb = collections.defaultdict(set)
for i, r in enumerate(B):
    cb[sum(r)].add(i)

ret = [-1] * 200
for i, r in enumerate(A):
    sa = sum(r)
    for idx in cb[sa]:
        if B[idx] == A[i]:
            ret[i] = idx
            cb[sa].discard(idx)
            break

print(ret)
print(sorted(list(set(ret))))
print(len(sorted(list(set(ret)))))