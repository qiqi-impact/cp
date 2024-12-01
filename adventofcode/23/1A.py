with open("in") as f:
    r = 0
    for x in f.read().splitlines():
        f = str(x)
        q = []

        st = ''
        for c in f:
            try:
                q.append(int(c))
                break
            except:
                pass
        p = ''
        for i in range(len(f)-1, -1, -1):
            try:
                q.append(int(f[i]))
                break
            except:
                pass
        print(q)

        r += (q[0]*10 + q[-1])
        print(q)
    print(r)