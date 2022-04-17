class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ret = ['']
            for i in range(len(s)):
                if len(ret[-1]) >= k:
                    ret.append('')
                ret[-1] += s[i]
            ret = [str(sum([int(c) for c in x])) for x in ret]
            s = ''.join(ret)
        return s