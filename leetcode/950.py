class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque([i for i in range(len(deck))])
        ret = []
        kill = True
        while q:
            cur = q.popleft()
            if not kill:
                q.append(cur)
            else:
                ret.append(cur)
            kill = not kill
        deck.sort()
        ans = [None] * len(deck)
        for i in range(len(deck)):
            ans[ret[i]] = deck[i]
        return ans
