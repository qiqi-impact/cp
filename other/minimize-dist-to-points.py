import random, math

N = 1
A = 0.0001
T = 0.75
points = []
for i in range(N):
    points.append((random.random(), random.random()))
print(points)

def gradient(x, y, isy):
    ret = 0
    for i in range(N):
        xi, yi = points[i]
        numerator = (y - yi) if isy else (x - xi)
        ret += numerator / math.dist((x, y), (xi, yi))
    return ret

def f(x, y):
    ret = 0
    for i in range(N):
        ret += math.dist((x, y), points[i])
    return ret

cur = [0.5, 0.5]
dif = 10**5
while dif > A*T:
    x, y = cur
    nx, ny = x, y
    nx -= A * gradient(x, y, 0)
    ny -= A * gradient(x, y, 1)
    A *= T
    dif = abs(f(x, y) - f(nx, ny))
    cur = [nx, ny]
print(cur)