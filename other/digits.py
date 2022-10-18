import math, collections

def digit_indexes(arr):
    n = len(arr)
    sz = int(math.log10(n)+1)
    # print(sz)
    q = collections.deque()
    cur = 0
    ret = []
    for i in range(n):
        idx = i + 1
        s = str(idx)
        q.append(arr[i])
        cur = 10 * cur + arr[i]
        if len(q) > sz:
            v = q.popleft()
            cur -= (10**sz) * v
        x = str(cur)
        # print(s, x)
        if x[-len(s):] == s:
            ret.append(idx)
    return ret

print(digit_indexes([3, 1, 4, 1, 5, 9, 2, 6, 1, 0]))