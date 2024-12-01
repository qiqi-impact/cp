from functools import cache

class Node:
    def __init__(self, v, idx):
        self.v = v
        self.idx = idx
        self.nx = self.pr = None

nums = []
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        v = int(l)
        nums.append(Node(v, i))

N = len(nums)
for i in range(N):
    nums[i].nx = nums[(i+1)%N]
    nums[i].pr = nums[(i-1)%N]

HEAD = nums[0]
TAIL = nums[-1]

def pr():
    ret = []
    cur = HEAD
    while 1:
        ret.append(cur.v)
        cur = cur.nx
        if cur == HEAD:
            break
    print(ret)

for i in range(N):
    cur = HEAD
    while cur.idx != i:
        cur = cur.nx
    x = cur.v

    if x > 0:
        for _ in range(x%(N-1)):
            cur.nx.v, cur.v = cur.v, cur.nx.v
            cur.nx.idx, cur.idx = cur.idx, cur.nx.idx
            cur = cur.nx
    else:
        for _ in range((-x)%(N-1)):
            cur.pr.v, cur.v = cur.v, cur.pr.v
            cur.pr.idx, cur.idx = cur.idx, cur.pr.idx
            cur = cur.pr

cur = HEAD
while cur.v != 0:
    cur = cur.nx

sm = 0
for j in range(3):
    for k in range(1000):
        cur = cur.nx
    sm += cur.v
    print(cur.v)
print(sm)