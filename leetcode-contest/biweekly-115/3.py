class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def check_ham(i, j):
            if groups[i] == groups[j]:
                return False
            if len(words[i]) != len(words[j]):
                return False
            a, b = words[i], words[j]
            r = 0
            for t in range(len(a)):
                r += a[t] != b[t]
                if r > 1:
                    return False
            return r == 1
        
        dp = []
        back = []
        best = 0
        q = None
        for i in range(len(words)):
            ret = 1
            bi = None
            for j in range(i):
                if check_ham(j, i) and ret < 1 + dp[j]:
                    ret = 1 + dp[j]
                    bi = j
            dp.append(ret)
            back.append(bi)
            if ret > best:
                best = ret
                q = i
        
        ret = []
        cur = q
        while cur is not None:
            ret.append(words[cur])
            cur = back[cur]
        return ret[::-1]
            
        