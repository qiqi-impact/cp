class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @cache
        def dfs(o, c):
            if c == 0:
                if o == 0:
                    return ['']
                else:
                    return []
            ret = []
            if c-o > 0:
                l = dfs(o, c-1)
                ret += [')'+x for x in l]
            if o > 0:
                l = dfs(o-1, c)
                ret += ['('+x for x in l]
            return ret
        return dfs(n, n)