import random
from collections import deque

def play_next(arr, q, k):
    idx = random.randint(0, len(arr)-1)
    arr[idx], arr[-1] = arr[-1], arr[idx]
    v = arr.pop()
    q.append(v)
    if len(q) > k:
        arr.append(q.popleft())
    return v

arr = ['A', 'B', 'C', 'D']
k = 3
q = deque()

print([play_next(arr, q, k) for _ in range(20)])