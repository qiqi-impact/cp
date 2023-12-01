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
            st += c
            if st[-3:] == 'one':
                q.append(1)
                break
            elif st[-3:] == 'two':
                q.append(2)
                break
            elif st[-5:] == 'three':
                q.append(3)
                break
            elif st[-4:] == 'four':
                q.append(4)
                break
            elif st[-4:] == 'five':
                q.append(5)
                break
            elif st[-3:] == 'six':
                q.append(6)
                break
            elif st[-5:] == 'seven':
                q.append(7)
                break
            elif st[-5:] == 'eight':
                q.append(8)
                break
            elif st[-4:] == 'nine':
                q.append(9)
                break
        p = ''
        for i in range(len(f)-1, -1, -1):
            try:
                q.append(int(f[i]))
                break
            except:
                pass
            p = f[i] + p
            if p.startswith('one'):
                q.append(1)
                break
            elif p.startswith('two'):
                q.append(2)
                break
            elif p.startswith('three'):
                q.append(3)
                break 
            elif p.startswith('four'):
                q.append(4)
                break
            elif p.startswith('five'):
                q.append(5)
                break
            elif p.startswith('six'):
                q.append(6)
                break
            elif p.startswith('seven'):
                q.append(7)
                break 
            elif p.startswith('eight'):
                q.append(8)
                break
            elif p.startswith('nine'):
                q.append(9)
                break
        print(f) 
        print(q)

        r += (q[0]*10 + q[-1])
        print(q)
    print(r)