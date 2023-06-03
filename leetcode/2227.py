class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.d = {}
        self.e = {}
        for i in range(len(keys)):
            k, v = keys[i], values[i]
            self.e[k] = v
            if v not in self.d:
                self.d[v] = []
            self.d[v].append(k)

        self.root = {}
        for w in dictionary:
            cur = self.root
            for i, c in enumerate(w):
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                if i == len(w)-1:
                    cur['exist'] = True

    def encrypt(self, word1: str) -> str:
        ret = []
        for k in word1:
            if k in self.e:
                ret.append(self.e[k])
            else:
                return ''
        return ''.join(ret)

    def dec(self, w, idx, node):
        if idx == len(w):
            return 'exist' in node
        t = w[idx:idx+2]
        if t not in self.d:
            return 0
        ret = 0
        for x in self.d[t]:
            if x in node:
                ret += self.dec(w, idx+2, node[x])
        return ret


    def decrypt(self, word2: str) -> int:
        return self.dec(word2, 0, self.root)


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)