class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        def computeLPSArray(pat, M, lps):
            len = 0  # length of the previous longest prefix suffix

            lps[0] = 0 # lps[0] is always 0
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
        l = [0] * len(s)
        computeLPSArray(s, len(s), l)
        
        lp = 0
        for i in range(len(s)-1, -1, -1):
            fail = False
            while s[i] != s[lp]:
                if lp == 0:
                    fail = True
                    break
                else:
                    lp = l[lp-1]
            if fail:
                continue
            if i - lp <= 1:
                return s[lp+i+1:][::-1] + s
            lp += 1
                
        
        
        