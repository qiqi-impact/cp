def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    ret = []
 
    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    j = 0  # index for pat[]
 
    # Preprocess the pattern (calculate lps[] array)
    lps = LPS(pat)
 
    i = 0  # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1
 
        if j == M:
            ret.append(i-j)
            j = lps[j-1]
 
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return ret

def LPS(word):
    lps = [0] * len(word)
    l = 0
    for i in range(1, len(word)):
        if word[l] == word[i]:
            l += 1
            lps[i] = l
        else:
            while l and word[i] != word[l]:
                l = lps[l-1]
            if word[i] == word[l]:
                l += 1
                lps[i] = l
    return lps

tc = [
    'aaaaa',
    'aaabaab',
    'abacaba',
]
for t in tc:
    print(KMPSearch('aa', t))