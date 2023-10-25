class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if a > b:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


def number_max_profit_groups(arr):
    n = len(arr)
    l = sorted(zip(arr, range(n)))
    uf = DisjointSetUnion(n)
    vis = [0] * n
    ret = 0
    for x, i in l:
        vis[i] = 1
        for j in i-1, i+1:
            if 0 <= j < n and vis[j]:
                uf.union(i, j)
        L = uf.find(i)
        R = L + uf.set_size(i) - 1
        ret += (i - L + 1) * (R - i + 1)
    return ret

print(number_max_profit_groups([3,1,3,5]))