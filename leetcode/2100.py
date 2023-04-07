class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        lni = [1] * n
        lnd = [1] * n
        for i in range(n):
            if i > 0 and security[i-1] >= security[i]:
                lni[i] = lni[i-1] + 1
        for i in range(n-1, -1, -1):
            if i < n-1 and security[i+1] >= security[i]:
                lnd[i] = lnd[i+1] + 1
        ret = []
        for i in range(time, n - time):
            if lni[i] >= time+1 and lnd[i] >= time+1:
                ret.append(i)
        return ret