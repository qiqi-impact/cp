class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts.sort()
            x = gifts.pop()
            gifts.append(int(math.sqrt(x)))
        return sum(gifts)