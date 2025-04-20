n = 100

# never use fenw[0]
fenw = [0] * (n+2)

# add delta to ith element
def update(i, delta):
    while i <= n:
        fenw[i] += delta
        i += i & -i

# return sum of the first i elements
def query_bit(i):
    total = 0
    while i:
        total += fenw[i]
        i -= i & -i
    return total

# add delta to query_bit(l)..query_bit(r-1)
def range_update(l,r,delta):
    update(l, delta)
    update(r, -delta)