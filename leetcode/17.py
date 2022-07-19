class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ret = ['']
        for c in digits:
            nr = []
            for x in ret:
                for y in d[int(c)]:
                    nr.append(x + y)
            ret = nr
        return ret