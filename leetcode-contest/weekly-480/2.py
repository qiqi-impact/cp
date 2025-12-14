class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) <= 1:
            return s
        words = s.split(' ')
        k = 0
        for c in words[0]:
            if c in 'aeiou':
                k += 1
        # print(k)
        ret = [words[0]]
        for w in words[1:]:
            t = 0
            for c in w:
                if c in 'aeiou':
                    t += 1
            if t == k:
                ret.append(w[::-1])
            else:
                ret.append(w)
        return ' '.join(ret)