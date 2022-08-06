class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for x, y in items1 + items2:
            d[x] += y
        return sorted(list(d.items()))