class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        f = defaultdict(int)
        for k in ranks:
            f[k] += 1
        t = max(list(f.values()))
        if t >= 3:
            return 'Three of a Kind'
        elif t == 2:
            return 'Pair'
        return 'High Card'