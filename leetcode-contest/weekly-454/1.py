class Solution:
    def generateTag(self, caption: str) -> str:
        l = caption.split(' ')
        n = len(l)
        ret = []
        first = True
        for i in range(n):
            if not l[i]:
                continue
            r = ''
            for c in l[i]:
                if c.isalpha():
                    r += c
            w = r.lower()
            if not first:
                w = w[0].upper() + w[1:]
            first = False
            ret.append(w)
        return ('#' + ''.join(ret))[:100]