class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split(' ')
        ret = 0
        for w in words:
            if len(w) == 0:
                continue
            if w.count('-') > 1:
                continue
            punc = 0
            fail = False
            for i in range(len(w)):
                if w[i] in '.,!':
                    if i != len(w) - 1:
                        fail = True
                        break
                    punc += 1
            if punc > 1 or fail:
                continue
            fail = False
            for i in range(len(w)):
                if w[i] == '-':
                    if i == 0 or i == len(w)-1 or not ('a' <= w[i-1] <= 'z') or not ('a' <= w[i+1] <= 'z'):
                        fail = True
                        break
                if '0' <= w[i] <= '9':
                    fail = True
                    break
            if fail:
                continue
            print(w)
            ret += 1
        return ret