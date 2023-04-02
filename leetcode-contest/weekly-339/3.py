class Solution:
    def miceAndCheese(self, a: List[int], b: List[int], k: int) -> int:
        df = [a[i] - b[i] for i in range(len(a))]
        df.sort(reverse=True)
        return sum(df[:k]) + sum(b)