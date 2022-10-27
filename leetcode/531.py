class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        R, C = len(picture), len(picture[0])
        r = defaultdict(set)
        c = defaultdict(set)
        for i in range(R):
            for j in range(C):
                if picture[i][j] == 'B':
                    r[i].add(j)
                    c[j].add(i)
        ret = 0
        for i in range(R):
            for j in range(C):
                if picture[i][j] == 'B' and len(r[i]) == 1 and len(c[j]) == 1:
                    ret += 1
        return ret