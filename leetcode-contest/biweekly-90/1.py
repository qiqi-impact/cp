class Solution:
    def oddString(self, words: List[str]) -> str:
        l = [[ord(c) for c in w] for w in words]
        d = defaultdict(int)
        for x in l:
            dif = []
            for i in range(len(x)-1):
                dif += [x[i+1] - x[i]]
                d[tuple(dif)] += 1
        for j, x in enumerate(l):
            dif = []
            for i in range(len(x)-1):
                dif += [x[i+1] - x[i]]
                if d[tuple(dif)] == 1:
                    return words[j]