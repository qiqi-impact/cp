class Solution:
    def reformatNumber(self, number: str) -> str:
        l = ''.join([c for c in number if c not in ' -'])
        lp = 0
        ret = ''
        while 1:
            left = len(l) - lp
            if left > 4:
                ret += l[lp:lp+3]+'-'
                lp += 3
            elif left < 4:
                ret += l[lp:]
                break
            else:
                ret += l[lp:lp+2] + '-' + l[lp+2:]
                break
        return ret