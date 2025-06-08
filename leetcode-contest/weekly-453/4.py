class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)

        @cache
        def ops(i, j, rev):
            if i == j:
                return int(word1[i] != word2[j])
            pairs = defaultdict(int)
            r = 0
            for x in range(i, j+1):
                cur = x
                if rev:
                    cur = j - (x - i)
                if word2[cur] == word1[x]:
                    continue
                if pairs[(word2[cur], word1[x])] > 0:
                    pairs[(word2[cur], word1[x])] -= 1
                else:
                    pairs[(word1[x], word2[cur])] += 1
                    r += 1
            # print(pairs)
            # print(i, j, rev, r)
            return r
        
        @cache
        def dp(i):
            if i == n:
                return 0
            ret = inf
            for j in range(i+1, n+1):
                ret = min(ret, ops(i, j-1, False) + dp(j), 1 + ops(i, j-1, True) + dp(j))
            return ret

        return dp(0)