from sortedcontainers import SortedList

class Solution:
    def totalStrength(self, A):
        MOD = 10**9+7
        n = len(A)
        
        lb = [-1] * n
        rb = [n] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                rb[stack[-1]] = i
                stack.pop()
            if stack:
                lb[i] = stack[-1]
            stack.append(i)
        
        ps = [0]
        pps = [0]
        for x in A:
            ps.append(ps[-1] + x)
            pps.append(pps[-1] + ps[-1])
            ps[-1] %= MOD
            pps[-1] %= MOD
        ops = [0] * (n+1)
        opps = [0] * (n+1)
        for i in range(n-1, -1, -1):
            ops[i] = ops[i+1] + A[i]
            opps[i] = opps[i+1] + ops[i]
            ops[i] %= MOD
            opps[i] %= MOD
        
        ret = 0
        for j in range(n):
            left, right = lb[j], rb[j]
            # print(j, left, right)
            lc = j - left
            rc = right - j - 1
            lsm = opps[left + 1] - opps[j + 1] - (j - left)*ops[j + 1]
            rsm = pps[right] - pps[j+1] - (right - j - 1)*ps[j+1]
            ret += A[j] * (lc * rsm + (rc+1) * lsm)
            ret = ((ret % MOD) + MOD) % MOD
            # print(lc, rc, lsm, rsm, ret)
        
        return ret