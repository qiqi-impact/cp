def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    ret = []
 
    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0  # index for pat[]
 
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
 
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

def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix
 
    lps[0] = 0  # lps[0] is always 0
    i = 1
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        p = ''.join([str(x+1) for x in pattern])
        s = ''
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                s += '2'
            elif nums[i] == nums[i-1]:
                s += '1'
            else:
                s += '0'
        return len(KMPSearch(p, s))