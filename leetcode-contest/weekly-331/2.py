class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l = [0]
        for w in words:
            l.append(l[-1] + int(w[0] in 'aeiou' and w[-1] in 'aeiou'))
        ret = []
        for x, y in queries:
            ret.append(l[y+1] - l[x])
        return ret