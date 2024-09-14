from collections import defaultdict

with open("in") as f:
    d = defaultdict(int)
    LEN = 4
    for x in f.read().splitlines():
        for i in range(len(x)-LEN+1):
            if len(set(x[i:i+LEN])) == LEN:
                print(i+LEN)
                break