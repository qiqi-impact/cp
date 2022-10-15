class Solution:
    def countTime(self, time: str) -> int:
        def match(a, b):
            for i in range(5):
                if not (a[i] == '?' or a[i] == b[i]):
                    return False
            return True
        
        ret = 0
        for h in range(24):
            for m in range(60):
                s = '{}:{}'.format(str(h).zfill(2), str(m).zfill(2))
                if match(time, s):
                    ret += 1
        return ret