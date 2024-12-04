with open("in") as f:
    ret = 0
    stacks = [[] for _ in range(10)]
    for x in f.read().splitlines():
        for c in range(0, len(x), 4):
            block = x[c:c+4]
            if '[' in block:
                stacks[c//4].insert(0, (block[1]))
        xx = x.split(' ')
        if 'move' in xx:
            params = [int(xx[1]), int(xx[3])-1, int(xx[5])-1]
            for x in range(params[0]):
                a = stacks[params[1]].pop()
                stacks[params[2]].append(a)
    for i in range(len(stacks)):
        print(stacks[i][-1] if stacks[i] else '', end="")