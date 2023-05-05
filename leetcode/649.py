from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        for i in range(len(senate)):
            a = r if senate[i] == 'R' else d
            a.append(i)
        while r and d:
            if r[0] < d[0]:
                r.append(len(senate)+r[0])
            else:
                d.append(len(senate)+d[0])
            r.popleft()
            d.popleft()
        return 'Radiant' if r else 'Dire'