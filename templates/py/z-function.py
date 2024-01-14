def zf(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(z[i-l], r - i)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z

def search_pattern(pattern, text):
    concatenated = pattern + "$" + text
    z = zf(concatenated)
    pattern_length = len(pattern)
    matches = []

    for i in range(len(concatenated)):
        if z[i] == pattern_length:
            matches.append(i - pattern_length - 1)

    return matches

tc = [
    'aaaaa',
    'aaabaab',
    'abacaba',
]
for t in tc:
    print(search_pattern('aa', t))