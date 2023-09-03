class Solution:
    def minimumOperations(self, num: str) -> int:
        ret = len(num) - num.count('0')
        for t in ['25', '50', '75', '00']:
            tp = 1
            cur = 0
            for i in range(len(num)-1, -1, -1):
                if num[i] == t[tp]:
                    tp -= 1
                    if tp == -1:
                        ret = min(ret, cur)
                        break
                else:
                    cur += 1
        return ret