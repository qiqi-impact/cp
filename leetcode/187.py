class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = defaultdict(int)
        for i in range(len(s)-9):
            d[s[i:i+10]] += 1
        return [x for x in d if d[x] > 1]