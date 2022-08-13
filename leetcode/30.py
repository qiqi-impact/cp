class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        mod = len(words[0])
        ct = []
        mp = {}
        for w in words:
            if w in mp:
                ct[mp[w]] += 1
            else:
                mp[w] = len(ct)
                ct.append(1)
        uniq = len(ct)
        ret = []
        for start in range(mod):
            word_index = [[0 for _ in range(uniq)]]
            for i in range(start, len(s), mod):
                t = s[i:i+mod]
                if t in mp:
                    word_index.append(word_index[-1][:])
                    word_index[-1][mp[t]] += 1
                    if len(word_index) >= len(words):
                        a = word_index[-1]
                        b = word_index[len(word_index)-1-len(words)]
                        fail = False
                        for j in range(uniq):
                            if a[j] - b[j] != ct[j]:
                                fail = True
                                break
                        if not fail:
                            ret.append(i - (len(words)-1)*mod)
                else:
                    word_index = word_index[:1]
        return ret