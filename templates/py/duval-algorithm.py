def duval(s):
    n = len(s)
    i = 0
    fac = []
    while i < n:
        j, k = i + 1, i
        while j < n and s[k] <= s[j]:
            if s[k] < s[j]:
                k = i
            else:
                k += 1
            j += 1
        while i <= k:
            fac.append(s[i:i+j-k])
            i += j - k
    return fac