'''
Dynamic programming solution to https://www.youtube.com/watch?v=iSNsgj1OCLA
===========================================================================

Number the boxes themselves 1-100.

Each prisoner looks at his numbered box, and sees the number in it, and goes to that box, so on and so forth 50 times. Therefore the likelihood that all the prisoners see their number is the likelihood that there is no cycle of length > 50 in the permutation mapping of (box# -> number under box).

The calculation is the interesting part.

Define P(n, k, limit) to be the probability that you can assign n boxes their value (given that there is an unclosed path of length k from previous assignments) without there being a cycle of length > limit.

Note that if k >= limit, then whenever we close the cycle with the head of the k-length path, we have a cycle of length > limit, so P(n, k, limit) = 0.

Also note that if n = 1 and k < limit, we are assigning 1 vertex to either connect with itself (if k = 0) or connect with a path of length < limit, which makes a cycle <= limit, so either case is acceptable and P(n, k, limit) = 1.

Otherwise, two cases:

1. The vertex loops back to itself (if k = 0) or the head of the unclosed path (if k > 0). This will leave zero unclosed vertices, and has a probability of 1/n, so this contributes 1/n*P(n-1, 0, limit). We can arbitrarily pick the next vertex to assign.

2. The vertex points to any other vertex. Probability (n-1)/n. This increases the size of the unclosed vertex path by 1, so this contributes (n-1)/n*P(n-1, k+1, limit). The next vertex we assign is this "other" vertex. 

This becomes a simple dynamic programming problem solvable in O(N^2).
'''

import functools

@functools.cache
def p(n, k, limit):
    if k >= limit:
        return 0
    if n == 1:
        return 1
    return 1/n*p(n-1, 0, limit) + (n-1)/n*p(n-1, k+1, limit)

for N in range(2, 102, 2):
    print(N, p(N, 0, N//2))