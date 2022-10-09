class Solution:
    def robotWithString(self, s: str) -> str:
        ct = Counter(s)
        a = [c for c in s][::-1]
        b = []
        ret = []
        for c in string.ascii_lowercase:
            while b and b[-1] <= c:
                ret.append(b.pop())
            while c in ct and ct[c] > 0:
                v = a.pop()
                ct[v] -= 1
                if v == c:
                    ret.append(v)
                else:
                    b.append(v)
        return ''.join(ret)