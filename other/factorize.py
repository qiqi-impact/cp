def fac(x):
    cur = x
    for i in range(2, 1+x//2):
        if i > cur:
            break
        while cur % i == 0:
            cur //= i
            print(i,)
    if cur > 1:
        print(cur,)

fac(730)