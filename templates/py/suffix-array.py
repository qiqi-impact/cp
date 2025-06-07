def build_suffix_array(s):
    s += '$'
    n = len(s)
    k = 0

    rank = [ord(c) for c in s]
    tmp = [0] * n
    sa = list(range(n))

    def radix_sort():
        cnt = [0] * (max(n, 256))
        for i in range(n):
            cnt[rank[i]] += 1
        for i in range(1, len(cnt)):
            cnt[i] += cnt[i - 1]
        sa2 = [0] * n
        for i in range(n - 1, -1, -1):
            cnt[rank[sa[i]]] -= 1
            sa2[cnt[rank[sa[i]]]] = sa[i]
        return sa2

    while True:
        key = lambda i: (rank[i], rank[i + (1 << k)] if i + (1 << k) < n else -1)
        sa.sort(key=key)

        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (key(sa[i - 1]) != key(sa[i]))
        rank = tmp[:]

        k += 1
        if (1 << k) >= n:
            break

    return sa

s = "banana"
sa = build_suffix_array(s)
print("Suffix Array:", sa)